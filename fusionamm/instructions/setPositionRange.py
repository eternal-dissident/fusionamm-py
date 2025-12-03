import borsh_construct as borsh
import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS
class SetPositionRangeArgs(typing.TypedDict):
    tickLowerIndex:int
    tickUpperIndex:int


layout = borsh.CStruct(
    "tickLowerIndex" /borsh.I32,
    "tickUpperIndex" /borsh.I32,
    )


class SetPositionRangeAccounts(typing.TypedDict):
    positionAuthority:SolPubkey
    position:SolPubkey
    positionTokenAccount:SolPubkey
    fusionPool:SolPubkey

def SetPositionRange(
    args: SetPositionRangeArgs,
    accounts: SetPositionRangeAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["positionAuthority"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["position"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["positionTokenAccount"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["fusionPool"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xc0\x16\xb0\xb0\x9b\x31\x99\x60"


    encoded_args = layout.build({
        "tickLowerIndex":args["tickLowerIndex"],
        "tickUpperIndex":args["tickUpperIndex"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



