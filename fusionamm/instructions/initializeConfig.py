import borsh_construct as borsh
import typing
from anchorpy.borsh_extension import BorshPubkey
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS
class InitializeConfigArgs(typing.TypedDict):
    feeAuthority:SolPubkey
    collectProtocolFeesAuthority:SolPubkey
    tokenBadgeAuthority:SolPubkey
    defaultProtocolFeeRate:int


layout = borsh.CStruct(
    "feeAuthority" /BorshPubkey,
    "collectProtocolFeesAuthority" /BorshPubkey,
    "tokenBadgeAuthority" /BorshPubkey,
    "defaultProtocolFeeRate" /borsh.U16,
    )


class InitializeConfigAccounts(typing.TypedDict):
    fusionPoolsConfig:SolPubkey
    funder:SolPubkey
    systemProgram:SolPubkey

def InitializeConfig(
    args: InitializeConfigArgs,
    accounts: InitializeConfigAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["fusionPoolsConfig"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["funder"], is_signer=True, is_writable=True),
    AccountMeta(pubkey=accounts["systemProgram"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xd0\x7f\x15\x01\xc2\xbe\xc4\x46"


    encoded_args = layout.build({
        "feeAuthority":args["feeAuthority"],
        "collectProtocolFeesAuthority":args["collectProtocolFeesAuthority"],
        "tokenBadgeAuthority":args["tokenBadgeAuthority"],
        "defaultProtocolFeeRate":args["defaultProtocolFeeRate"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)




