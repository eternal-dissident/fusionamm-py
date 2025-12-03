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


class PositionJSON(typing.TypedDict):
    version: int
    fusionPool: str
    positionMint: str
    liquidity: int
    tickLowerIndex: int
    tickUpperIndex: int
    feeGrowthCheckpointA: int
    feeOwedA: int
    feeGrowthCheckpointB: int
    feeOwedB: int
    reserved: list[int]

@dataclass
class Position:
    #fields
    version: int
    fusionPool: SolPubkey
    positionMint: SolPubkey
    liquidity: int
    tickLowerIndex: int
    tickUpperIndex: int
    feeGrowthCheckpointA: int
    feeOwedA: int
    feeGrowthCheckpointB: int
    feeOwedB: int
    reserved: bytes

    discriminator: typing.ClassVar = b"\xaa\xbc\x8f\xe4\x7a\x40\xf7\xd0"
    DISCRIMINATOR_SIZE: int = 8

    layout: typing.ClassVar = borsh.CStruct(
        "version" /borsh.U16,
        "fusionPool" /BorshPubkey,
        "positionMint" /BorshPubkey,
        "liquidity" /borsh.U128,
        "tickLowerIndex" /borsh.I32,
        "tickUpperIndex" /borsh.I32,
        "feeGrowthCheckpointA" /borsh.U128,
        "feeOwedA" /borsh.U64,
        "feeGrowthCheckpointB" /borsh.U128,
        "feeOwedB" /borsh.U64,
        "reserved" /FixedSizeBytes(128,GreedyBytes),
        )



    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: SolPubkey,
        commitment: typing.Optional[Commitment] = None,
        program_id: SolPubkey = FUSIONAMM_PROGRAM_ADDRESS,
    ) -> typing.Optional["Position"]:
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
    ) -> typing.List[typing.Optional["Position"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["Position"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != program_id:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "Position":
        if data[:cls.DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = Position.layout.parse(data[cls.DISCRIMINATOR_SIZE:])
        return cls(
                version=dec.version,
                fusionPool=dec.fusionPool,
                positionMint=dec.positionMint,
                liquidity=dec.liquidity,
                tickLowerIndex=dec.tickLowerIndex,
                tickUpperIndex=dec.tickUpperIndex,
                feeGrowthCheckpointA=dec.feeGrowthCheckpointA,
                feeOwedA=dec.feeOwedA,
                feeGrowthCheckpointB=dec.feeGrowthCheckpointB,
                feeOwedB=dec.feeOwedB,
                reserved=dec.reserved,
                )
    def to_encodable(self) -> dict[str, typing.Any]:
        return {
                "version": self.version,
                "fusionPool": self.fusionPool,
                "positionMint": self.positionMint,
                "liquidity": self.liquidity,
                "tickLowerIndex": self.tickLowerIndex,
                "tickUpperIndex": self.tickUpperIndex,
                "feeGrowthCheckpointA": self.feeGrowthCheckpointA,
                "feeOwedA": self.feeOwedA,
                "feeGrowthCheckpointB": self.feeGrowthCheckpointB,
                "feeOwedB": self.feeOwedB,
                "reserved": self.reserved,
                }
    def to_json(self) -> PositionJSON:
        return {
                "version": self.version,
                "fusionPool": str(self.fusionPool),
                "positionMint": str(self.positionMint),
                "liquidity": self.liquidity,
                "tickLowerIndex": self.tickLowerIndex,
                "tickUpperIndex": self.tickUpperIndex,
                "feeGrowthCheckpointA": self.feeGrowthCheckpointA,
                "feeOwedA": self.feeOwedA,
                "feeGrowthCheckpointB": self.feeGrowthCheckpointB,
                "feeOwedB": self.feeOwedB,
                "reserved": list(self.reserved),
                }

    @classmethod
    def from_json(cls, obj: PositionJSON) -> "Position":
        return cls(
                version=obj["version"],
                fusionPool=SolPubkey.from_string(obj["fusionPool"]),
                positionMint=SolPubkey.from_string(obj["positionMint"]),
                liquidity=obj["liquidity"],
                tickLowerIndex=obj["tickLowerIndex"],
                tickUpperIndex=obj["tickUpperIndex"],
                feeGrowthCheckpointA=obj["feeGrowthCheckpointA"],
                feeOwedA=obj["feeOwedA"],
                feeGrowthCheckpointB=obj["feeGrowthCheckpointB"],
                feeOwedB=obj["feeOwedB"],
                reserved=bytes(obj["reserved"]),
                )




