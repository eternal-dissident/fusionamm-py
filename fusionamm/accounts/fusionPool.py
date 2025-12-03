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


class FusionPoolJSON(typing.TypedDict):
    bump: list[int]
    version: int
    tokenMintA: str
    tokenMintB: str
    tokenVaultA: str
    tokenVaultB: str
    tickSpacing: int
    tickSpacingSeed: list[int]
    feeRate: int
    protocolFeeRate: int
    unused0: int
    liquidity: int
    sqrtPrice: int
    tickCurrentIndex: int
    protocolFeeOwedA: int
    protocolFeeOwedB: int
    feeGrowthGlobalA: int
    feeGrowthGlobalB: int
    ordersTotalAmountA: int
    ordersTotalAmountB: int
    ordersFilledAmountA: int
    ordersFilledAmountB: int
    olpFeeOwedA: int
    olpFeeOwedB: int
    maSqrtPrice: int
    lastSwapTimestamp: int
    reserved: list[int]

@dataclass
class FusionPool:
    #fields
    bump: bytes
    version: int
    tokenMintA: SolPubkey
    tokenMintB: SolPubkey
    tokenVaultA: SolPubkey
    tokenVaultB: SolPubkey
    tickSpacing: int
    tickSpacingSeed: bytes
    feeRate: int
    protocolFeeRate: int
    unused0: int
    liquidity: int
    sqrtPrice: int
    tickCurrentIndex: int
    protocolFeeOwedA: int
    protocolFeeOwedB: int
    feeGrowthGlobalA: int
    feeGrowthGlobalB: int
    ordersTotalAmountA: int
    ordersTotalAmountB: int
    ordersFilledAmountA: int
    ordersFilledAmountB: int
    olpFeeOwedA: int
    olpFeeOwedB: int
    maSqrtPrice: int
    lastSwapTimestamp: int
    reserved: bytes

    discriminator: typing.ClassVar = b"\xfe\xcc\xcf\x62\x19\xb5\x1d\x43"
    DISCRIMINATOR_SIZE: int = 8

    layout: typing.ClassVar = borsh.CStruct(
        "bump" /FixedSizeBytes(1,GreedyBytes),
        "version" /borsh.U16,
        "tokenMintA" /BorshPubkey,
        "tokenMintB" /BorshPubkey,
        "tokenVaultA" /BorshPubkey,
        "tokenVaultB" /BorshPubkey,
        "tickSpacing" /borsh.U16,
        "tickSpacingSeed" /FixedSizeBytes(2,GreedyBytes),
        "feeRate" /borsh.U16,
        "protocolFeeRate" /borsh.U16,
        "unused0" /borsh.U32,
        "liquidity" /borsh.U128,
        "sqrtPrice" /borsh.U128,
        "tickCurrentIndex" /borsh.I32,
        "protocolFeeOwedA" /borsh.U64,
        "protocolFeeOwedB" /borsh.U64,
        "feeGrowthGlobalA" /borsh.U128,
        "feeGrowthGlobalB" /borsh.U128,
        "ordersTotalAmountA" /borsh.U64,
        "ordersTotalAmountB" /borsh.U64,
        "ordersFilledAmountA" /borsh.U64,
        "ordersFilledAmountB" /borsh.U64,
        "olpFeeOwedA" /borsh.U64,
        "olpFeeOwedB" /borsh.U64,
        "maSqrtPrice" /borsh.U128,
        "lastSwapTimestamp" /borsh.U64,
        "reserved" /FixedSizeBytes(116,GreedyBytes),
        )



    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: SolPubkey,
        commitment: typing.Optional[Commitment] = None,
        program_id: SolPubkey = FUSIONAMM_PROGRAM_ADDRESS,
    ) -> typing.Optional["FusionPool"]:
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
    ) -> typing.List[typing.Optional["FusionPool"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["FusionPool"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != program_id:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "FusionPool":
        if data[:cls.DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = FusionPool.layout.parse(data[cls.DISCRIMINATOR_SIZE:])
        return cls(
                bump=dec.bump,
                version=dec.version,
                tokenMintA=dec.tokenMintA,
                tokenMintB=dec.tokenMintB,
                tokenVaultA=dec.tokenVaultA,
                tokenVaultB=dec.tokenVaultB,
                tickSpacing=dec.tickSpacing,
                tickSpacingSeed=dec.tickSpacingSeed,
                feeRate=dec.feeRate,
                protocolFeeRate=dec.protocolFeeRate,
                unused0=dec.unused0,
                liquidity=dec.liquidity,
                sqrtPrice=dec.sqrtPrice,
                tickCurrentIndex=dec.tickCurrentIndex,
                protocolFeeOwedA=dec.protocolFeeOwedA,
                protocolFeeOwedB=dec.protocolFeeOwedB,
                feeGrowthGlobalA=dec.feeGrowthGlobalA,
                feeGrowthGlobalB=dec.feeGrowthGlobalB,
                ordersTotalAmountA=dec.ordersTotalAmountA,
                ordersTotalAmountB=dec.ordersTotalAmountB,
                ordersFilledAmountA=dec.ordersFilledAmountA,
                ordersFilledAmountB=dec.ordersFilledAmountB,
                olpFeeOwedA=dec.olpFeeOwedA,
                olpFeeOwedB=dec.olpFeeOwedB,
                maSqrtPrice=dec.maSqrtPrice,
                lastSwapTimestamp=dec.lastSwapTimestamp,
                reserved=dec.reserved,
                )
    def to_encodable(self) -> dict[str, typing.Any]:
        return {
                "bump": self.bump,
                "version": self.version,
                "tokenMintA": self.tokenMintA,
                "tokenMintB": self.tokenMintB,
                "tokenVaultA": self.tokenVaultA,
                "tokenVaultB": self.tokenVaultB,
                "tickSpacing": self.tickSpacing,
                "tickSpacingSeed": self.tickSpacingSeed,
                "feeRate": self.feeRate,
                "protocolFeeRate": self.protocolFeeRate,
                "unused0": self.unused0,
                "liquidity": self.liquidity,
                "sqrtPrice": self.sqrtPrice,
                "tickCurrentIndex": self.tickCurrentIndex,
                "protocolFeeOwedA": self.protocolFeeOwedA,
                "protocolFeeOwedB": self.protocolFeeOwedB,
                "feeGrowthGlobalA": self.feeGrowthGlobalA,
                "feeGrowthGlobalB": self.feeGrowthGlobalB,
                "ordersTotalAmountA": self.ordersTotalAmountA,
                "ordersTotalAmountB": self.ordersTotalAmountB,
                "ordersFilledAmountA": self.ordersFilledAmountA,
                "ordersFilledAmountB": self.ordersFilledAmountB,
                "olpFeeOwedA": self.olpFeeOwedA,
                "olpFeeOwedB": self.olpFeeOwedB,
                "maSqrtPrice": self.maSqrtPrice,
                "lastSwapTimestamp": self.lastSwapTimestamp,
                "reserved": self.reserved,
                }
    def to_json(self) -> FusionPoolJSON:
        return {
                "bump": list(self.bump),
                "version": self.version,
                "tokenMintA": str(self.tokenMintA),
                "tokenMintB": str(self.tokenMintB),
                "tokenVaultA": str(self.tokenVaultA),
                "tokenVaultB": str(self.tokenVaultB),
                "tickSpacing": self.tickSpacing,
                "tickSpacingSeed": list(self.tickSpacingSeed),
                "feeRate": self.feeRate,
                "protocolFeeRate": self.protocolFeeRate,
                "unused0": self.unused0,
                "liquidity": self.liquidity,
                "sqrtPrice": self.sqrtPrice,
                "tickCurrentIndex": self.tickCurrentIndex,
                "protocolFeeOwedA": self.protocolFeeOwedA,
                "protocolFeeOwedB": self.protocolFeeOwedB,
                "feeGrowthGlobalA": self.feeGrowthGlobalA,
                "feeGrowthGlobalB": self.feeGrowthGlobalB,
                "ordersTotalAmountA": self.ordersTotalAmountA,
                "ordersTotalAmountB": self.ordersTotalAmountB,
                "ordersFilledAmountA": self.ordersFilledAmountA,
                "ordersFilledAmountB": self.ordersFilledAmountB,
                "olpFeeOwedA": self.olpFeeOwedA,
                "olpFeeOwedB": self.olpFeeOwedB,
                "maSqrtPrice": self.maSqrtPrice,
                "lastSwapTimestamp": self.lastSwapTimestamp,
                "reserved": list(self.reserved),
                }

    @classmethod
    def from_json(cls, obj: FusionPoolJSON) -> "FusionPool":
        return cls(
                bump=bytes(obj["bump"]),
                version=obj["version"],
                tokenMintA=SolPubkey.from_string(obj["tokenMintA"]),
                tokenMintB=SolPubkey.from_string(obj["tokenMintB"]),
                tokenVaultA=SolPubkey.from_string(obj["tokenVaultA"]),
                tokenVaultB=SolPubkey.from_string(obj["tokenVaultB"]),
                tickSpacing=obj["tickSpacing"],
                tickSpacingSeed=bytes(obj["tickSpacingSeed"]),
                feeRate=obj["feeRate"],
                protocolFeeRate=obj["protocolFeeRate"],
                unused0=obj["unused0"],
                liquidity=obj["liquidity"],
                sqrtPrice=obj["sqrtPrice"],
                tickCurrentIndex=obj["tickCurrentIndex"],
                protocolFeeOwedA=obj["protocolFeeOwedA"],
                protocolFeeOwedB=obj["protocolFeeOwedB"],
                feeGrowthGlobalA=obj["feeGrowthGlobalA"],
                feeGrowthGlobalB=obj["feeGrowthGlobalB"],
                ordersTotalAmountA=obj["ordersTotalAmountA"],
                ordersTotalAmountB=obj["ordersTotalAmountB"],
                ordersFilledAmountA=obj["ordersFilledAmountA"],
                ordersFilledAmountB=obj["ordersFilledAmountB"],
                olpFeeOwedA=obj["olpFeeOwedA"],
                olpFeeOwedB=obj["olpFeeOwedB"],
                maSqrtPrice=obj["maSqrtPrice"],
                lastSwapTimestamp=obj["lastSwapTimestamp"],
                reserved=bytes(obj["reserved"]),
                )




