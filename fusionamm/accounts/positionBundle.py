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


class PositionBundleJSON(typing.TypedDict):
    positionBundleMint: str
    positionBitmap: list[int]

@dataclass
class PositionBundle:
    #fields
    positionBundleMint: SolPubkey
    positionBitmap: bytes

    discriminator: typing.ClassVar = b"\x81\xa9\xaf\x41\xb9\x5f\x20\x64"
    DISCRIMINATOR_SIZE: int = 8

    layout: typing.ClassVar = borsh.CStruct(
        "positionBundleMint" /BorshPubkey,
        "positionBitmap" /FixedSizeBytes(32,GreedyBytes),
        )



    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: SolPubkey,
        commitment: typing.Optional[Commitment] = None,
        program_id: SolPubkey = FUSIONAMM_PROGRAM_ADDRESS,
    ) -> typing.Optional["PositionBundle"]:
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
    ) -> typing.List[typing.Optional["PositionBundle"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["PositionBundle"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != program_id:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "PositionBundle":
        if data[:cls.DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = PositionBundle.layout.parse(data[cls.DISCRIMINATOR_SIZE:])
        return cls(
                positionBundleMint=dec.positionBundleMint,
                positionBitmap=dec.positionBitmap,
                )
    def to_encodable(self) -> dict[str, typing.Any]:
        return {
                "positionBundleMint": self.positionBundleMint,
                "positionBitmap": self.positionBitmap,
                }
    def to_json(self) -> PositionBundleJSON:
        return {
                "positionBundleMint": str(self.positionBundleMint),
                "positionBitmap": list(self.positionBitmap),
                }

    @classmethod
    def from_json(cls, obj: PositionBundleJSON) -> "PositionBundle":
        return cls(
                positionBundleMint=SolPubkey.from_string(obj["positionBundleMint"]),
                positionBitmap=bytes(obj["positionBitmap"]),
                )




