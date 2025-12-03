import borsh_construct as borsh
import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS
class SetProtocolFeeRateArgs(typing.TypedDict):
    protocolFeeRate:int


layout = borsh.CStruct(
    "protocolFeeRate" /borsh.U16,
    )


class SetProtocolFeeRateAccounts(typing.TypedDict):
    fusionPoolsConfig:SolPubkey
    fusionPool:SolPubkey
    feeAuthority:SolPubkey

def SetProtocolFeeRate(
    args: SetProtocolFeeRateArgs,
    accounts: SetProtocolFeeRateAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["fusionPoolsConfig"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["fusionPool"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["feeAuthority"], is_signer=True, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x5f\x07\x04\x32\x9a\x4f\x9c\x83"


    encoded_args = layout.build({
        "protocolFeeRate":args["protocolFeeRate"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



