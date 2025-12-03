import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS

class DeletePositionBundleAccounts(typing.TypedDict):
    positionBundle:SolPubkey
    positionBundleMint:SolPubkey
    positionBundleTokenAccount:SolPubkey
    positionBundleOwner:SolPubkey
    receiver:SolPubkey
    tokenProgram:SolPubkey

def DeletePositionBundle(
    accounts: DeletePositionBundleAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["positionBundle"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["positionBundleMint"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["positionBundleTokenAccount"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["positionBundleOwner"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["receiver"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenProgram"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x64\x19\x63\x02\xd9\xef\x7c\xad"


    encoded_args = b""
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)




