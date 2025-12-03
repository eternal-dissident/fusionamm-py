import borsh_construct as borsh
import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS
class CloseBundledPositionArgs(typing.TypedDict):
    bundleIndex:int


layout = borsh.CStruct(
    "bundleIndex" /borsh.U16,
    )


class CloseBundledPositionAccounts(typing.TypedDict):
    bundledPosition:SolPubkey
    positionBundle:SolPubkey
    positionBundleTokenAccount:SolPubkey
    positionBundleAuthority:SolPubkey
    receiver:SolPubkey

def CloseBundledPosition(
    args: CloseBundledPositionArgs,
    accounts: CloseBundledPositionAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["bundledPosition"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["positionBundle"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["positionBundleTokenAccount"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["positionBundleAuthority"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["receiver"], is_signer=False, is_writable=True),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x29\x24\xd8\xf5\x1b\x55\x67\x43"


    encoded_args = layout.build({
        "bundleIndex":args["bundleIndex"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



