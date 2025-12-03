import borsh_construct as borsh
import typing
from anchorpy.borsh_extension import BorshPubkey
from anchorpy.error import AccountInvalidDiscriminator
from anchorpy.utils.rpc import get_multiple_accounts
from dataclasses import dataclass
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Commitment
from solders.pubkey import Pubkey as SolPubkey
from .. import types
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS


class TickArrayJSON(typing.TypedDict):
    startTickIndex: int
    ticks: list[types.tick.TickJSON]
    fusionPool: str

@dataclass
class TickArray:
    #fields
    startTickIndex: int
    ticks: list[types.tick.Tick]
    fusionPool: SolPubkey

    discriminator: typing.ClassVar = b"\x45\x61\xbd\xbe\x6e\x07\x42\xbb"
    DISCRIMINATOR_SIZE: int = 8

    layout: typing.ClassVar = borsh.CStruct(
        "startTickIndex" /borsh.I32,
        "ticks" /types.tick.Tick.layout[88],
        "fusionPool" /BorshPubkey,
        )



    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: SolPubkey,
        commitment: typing.Optional[Commitment] = None,
        program_id: SolPubkey = FUSIONAMM_PROGRAM_ADDRESS,
    ) -> typing.Optional["TickArray"]:
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
    ) -> typing.List[typing.Optional["TickArray"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["TickArray"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != program_id:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "TickArray":
        if data[:cls.DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = TickArray.layout.parse(data[cls.DISCRIMINATOR_SIZE:])
        return cls(
                startTickIndex=dec.startTickIndex,
                ticks=list(map(lambda item:types.tick.Tick.from_decoded(item),dec.ticks)),
                fusionPool=dec.fusionPool,
                )
    def to_encodable(self) -> dict[str, typing.Any]:
        return {
                "startTickIndex": self.startTickIndex,
                "ticks": list(map(lambda item:item.to_encodable(),self.ticks)),
                "fusionPool": self.fusionPool,
                }
    def to_json(self) -> TickArrayJSON:
        return {
                "startTickIndex": self.startTickIndex,
                "ticks": list(map(lambda item:item.to_json(),self.ticks)),
                "fusionPool": str(self.fusionPool),
                }

    @classmethod
    def from_json(cls, obj: TickArrayJSON) -> "TickArray":
        return cls(
                startTickIndex=obj["startTickIndex"],
                ticks=list(map(lambda item:types.tick.Tick.from_json(item),obj["ticks"])),
                fusionPool=SolPubkey.from_string(obj["fusionPool"]),
                )




