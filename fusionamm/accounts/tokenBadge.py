import borsh_construct as borsh
import typing
from anchorpy.borsh_extension import BorshPubkey
from anchorpy.error import AccountInvalidDiscriminator
from anchorpy.utils.rpc import get_multiple_accounts
from construct import GreedyBytes
from dataclasses import dataclass
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Commitment
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS
from ..shared import FixedSizeBytes


class TokenBadgeJSON(typing.TypedDict):
    tokenMint: str
    reserved: list[int]

@dataclass
class TokenBadge:
    #fields
    tokenMint: SolPubkey
    reserved: bytes

    discriminator: typing.ClassVar = b"\x74\xdb\xcc\xe5\xf9\x74\xff\x96"
    DISCRIMINATOR_SIZE: int = 8

    layout: typing.ClassVar = borsh.CStruct(
        "tokenMint" /BorshPubkey,
        "reserved" /FixedSizeBytes(128,GreedyBytes),
        )



    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: SolPubkey,
        commitment: typing.Optional[Commitment] = None,
        program_id: SolPubkey = FUSIONAMM_PROGRAM_ADDRESS,
    ) -> typing.Optional["TokenBadge"]:
        resp = await conn.get_account_info(address, commitment=commitment)
        info = resp.value
        if info is None:
            return None
        if info.owner != program_id:
            raise ValueError("Account does not belong to this program")
        bytes_data = info.data
        return cls.decode(bytes_data)

    @classmethod
    async def fetch_multiple(
        cls,
        conn: AsyncClient,
        addresses: list[SolPubkey],
        commitment: typing.Optional[Commitment] = None,
        program_id: SolPubkey = FUSIONAMM_PROGRAM_ADDRESS,
    ) -> typing.List[typing.Optional["TokenBadge"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["TokenBadge"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != program_id:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "TokenBadge":
        if data[:cls.DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = TokenBadge.layout.parse(data[cls.DISCRIMINATOR_SIZE:])
        return cls(
                tokenMint=dec.tokenMint,
                reserved=dec.reserved,
                )
    def to_encodable(self) -> dict[str, typing.Any]:
        return {
                "tokenMint": self.tokenMint,
                "reserved": self.reserved,
                }
    def to_json(self) -> TokenBadgeJSON:
        return {
                "tokenMint": str(self.tokenMint),
                "reserved": list(self.reserved),
                }

    @classmethod
    def from_json(cls, obj: TokenBadgeJSON) -> "TokenBadge":
        return cls(
                tokenMint=SolPubkey.from_string(obj["tokenMint"]),
                reserved=bytes(obj["reserved"]),
                )




