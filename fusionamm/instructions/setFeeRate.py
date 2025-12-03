import borsh_construct as borsh
import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS
class SetFeeRateArgs(typing.TypedDict):
    feeRate:int


layout = borsh.CStruct(
    "feeRate" /borsh.U16,
    )


class SetFeeRateAccounts(typing.TypedDict):
    fusionPoolsConfig:SolPubkey
    fusionPool:SolPubkey
    feeAuthority:SolPubkey

def SetFeeRate(
    args: SetFeeRateArgs,
    accounts: SetFeeRateAccounts,
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
    identifier = b"\x35\xf3\x89\x41\x08\x8c\x9e\x06"


    encoded_args = layout.build({
        "feeRate":args["feeRate"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



