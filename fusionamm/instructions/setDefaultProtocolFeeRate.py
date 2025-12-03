import borsh_construct as borsh
import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS
class SetDefaultProtocolFeeRateArgs(typing.TypedDict):
    defaultProtocolFeeRate:int


layout = borsh.CStruct(
    "defaultProtocolFeeRate" /borsh.U16,
    )


class SetDefaultProtocolFeeRateAccounts(typing.TypedDict):
    fusionPoolsConfig:SolPubkey
    feeAuthority:SolPubkey

def SetDefaultProtocolFeeRate(
    args: SetDefaultProtocolFeeRateArgs,
    accounts: SetDefaultProtocolFeeRateAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["fusionPoolsConfig"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["feeAuthority"], is_signer=True, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x6b\xcd\xf9\xe2\x97\x23\x56\x00"


    encoded_args = layout.build({
        "defaultProtocolFeeRate":args["defaultProtocolFeeRate"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



