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


class LimitOrderJSON(typing.TypedDict):
    version: int
    fusionPool: str
    limitOrderMint: str
    tickIndex: int
    amount: int
    aToB: bool
    age: int
    reserved: list[int]

@dataclass
class LimitOrder:
    #fields
    version: int
    fusionPool: SolPubkey
    limitOrderMint: SolPubkey
    tickIndex: int
    amount: int
    aToB: bool
    age: int
    reserved: bytes

    discriminator: typing.ClassVar = b"\x89\xb7\xd4\x5b\x73\x1d\x8d\xe3"
    DISCRIMINATOR_SIZE: int = 8

    layout: typing.ClassVar = borsh.CStruct(
        "version" /borsh.U16,
        "fusionPool" /BorshPubkey,
        "limitOrderMint" /BorshPubkey,
        "tickIndex" /borsh.I32,
        "amount" /borsh.U64,
        "aToB" /borsh.Bool,
        "age" /borsh.U64,
        "reserved" /FixedSizeBytes(128,GreedyBytes),
        )



    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: SolPubkey,
        commitment: typing.Optional[Commitment] = None,
        program_id: SolPubkey = FUSIONAMM_PROGRAM_ADDRESS,
    ) -> typing.Optional["LimitOrder"]:
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
    ) -> typing.List[typing.Optional["LimitOrder"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["LimitOrder"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != program_id:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "LimitOrder":
        if data[:cls.DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = LimitOrder.layout.parse(data[cls.DISCRIMINATOR_SIZE:])
        return cls(
                version=dec.version,
                fusionPool=dec.fusionPool,
                limitOrderMint=dec.limitOrderMint,
                tickIndex=dec.tickIndex,
                amount=dec.amount,
                aToB=dec.aToB,
                age=dec.age,
                reserved=dec.reserved,
                )
    def to_encodable(self) -> dict[str, typing.Any]:
        return {
                "version": self.version,
                "fusionPool": self.fusionPool,
                "limitOrderMint": self.limitOrderMint,
                "tickIndex": self.tickIndex,
                "amount": self.amount,
                "aToB": self.aToB,
                "age": self.age,
                "reserved": self.reserved,
                }
    def to_json(self) -> LimitOrderJSON:
        return {
                "version": self.version,
                "fusionPool": str(self.fusionPool),
                "limitOrderMint": str(self.limitOrderMint),
                "tickIndex": self.tickIndex,
                "amount": self.amount,
                "aToB": self.aToB,
                "age": self.age,
                "reserved": list(self.reserved),
                }

    @classmethod
    def from_json(cls, obj: LimitOrderJSON) -> "LimitOrder":
        return cls(
                version=obj["version"],
                fusionPool=SolPubkey.from_string(obj["fusionPool"]),
                limitOrderMint=SolPubkey.from_string(obj["limitOrderMint"]),
                tickIndex=obj["tickIndex"],
                amount=obj["amount"],
                aToB=obj["aToB"],
                age=obj["age"],
                reserved=bytes(obj["reserved"]),
                )




