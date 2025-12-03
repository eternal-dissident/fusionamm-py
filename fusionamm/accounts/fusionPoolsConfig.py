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


class FusionPoolsConfigJSON(typing.TypedDict):
    version: int
    feeAuthority: str
    collectProtocolFeesAuthority: str
    tokenBadgeAuthority: str
    defaultProtocolFeeRate: int
    unused0: int
    unused1: int
    reserved: list[int]

@dataclass
class FusionPoolsConfig:
    #fields
    version: int
    feeAuthority: SolPubkey
    collectProtocolFeesAuthority: SolPubkey
    tokenBadgeAuthority: SolPubkey
    defaultProtocolFeeRate: int
    unused0: int
    unused1: int
    reserved: bytes

    discriminator: typing.ClassVar = b"\xbf\xc7\x13\x0b\x4b\x56\xef\xa9"
    DISCRIMINATOR_SIZE: int = 8

    layout: typing.ClassVar = borsh.CStruct(
        "version" /borsh.U16,
        "feeAuthority" /BorshPubkey,
        "collectProtocolFeesAuthority" /BorshPubkey,
        "tokenBadgeAuthority" /BorshPubkey,
        "defaultProtocolFeeRate" /borsh.U16,
        "unused0" /borsh.U16,
        "unused1" /borsh.U16,
        "reserved" /FixedSizeBytes(170,GreedyBytes),
        )



    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: SolPubkey,
        commitment: typing.Optional[Commitment] = None,
        program_id: SolPubkey = FUSIONAMM_PROGRAM_ADDRESS,
    ) -> typing.Optional["FusionPoolsConfig"]:
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
    ) -> typing.List[typing.Optional["FusionPoolsConfig"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["FusionPoolsConfig"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != program_id:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "FusionPoolsConfig":
        if data[:cls.DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = FusionPoolsConfig.layout.parse(data[cls.DISCRIMINATOR_SIZE:])
        return cls(
                version=dec.version,
                feeAuthority=dec.feeAuthority,
                collectProtocolFeesAuthority=dec.collectProtocolFeesAuthority,
                tokenBadgeAuthority=dec.tokenBadgeAuthority,
                defaultProtocolFeeRate=dec.defaultProtocolFeeRate,
                unused0=dec.unused0,
                unused1=dec.unused1,
                reserved=dec.reserved,
                )
    def to_encodable(self) -> dict[str, typing.Any]:
        return {
                "version": self.version,
                "feeAuthority": self.feeAuthority,
                "collectProtocolFeesAuthority": self.collectProtocolFeesAuthority,
                "tokenBadgeAuthority": self.tokenBadgeAuthority,
                "defaultProtocolFeeRate": self.defaultProtocolFeeRate,
                "unused0": self.unused0,
                "unused1": self.unused1,
                "reserved": self.reserved,
                }
    def to_json(self) -> FusionPoolsConfigJSON:
        return {
                "version": self.version,
                "feeAuthority": str(self.feeAuthority),
                "collectProtocolFeesAuthority": str(self.collectProtocolFeesAuthority),
                "tokenBadgeAuthority": str(self.tokenBadgeAuthority),
                "defaultProtocolFeeRate": self.defaultProtocolFeeRate,
                "unused0": self.unused0,
                "unused1": self.unused1,
                "reserved": list(self.reserved),
                }

    @classmethod
    def from_json(cls, obj: FusionPoolsConfigJSON) -> "FusionPoolsConfig":
        return cls(
                version=obj["version"],
                feeAuthority=SolPubkey.from_string(obj["feeAuthority"]),
                collectProtocolFeesAuthority=SolPubkey.from_string(obj["collectProtocolFeesAuthority"]),
                tokenBadgeAuthority=SolPubkey.from_string(obj["tokenBadgeAuthority"]),
                defaultProtocolFeeRate=obj["defaultProtocolFeeRate"],
                unused0=obj["unused0"],
                unused1=obj["unused1"],
                reserved=bytes(obj["reserved"]),
                )




