import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS

class DeleteTokenBadgeAccounts(typing.TypedDict):
    fusionPoolsConfig:SolPubkey
    tokenBadgeAuthority:SolPubkey
    tokenMint:SolPubkey
    tokenBadge:SolPubkey
    receiver:SolPubkey

def DeleteTokenBadge(
    accounts: DeleteTokenBadgeAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["fusionPoolsConfig"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenBadgeAuthority"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["tokenMint"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenBadge"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["receiver"], is_signer=False, is_writable=True),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x35\x92\x44\x08\x12\x75\x11\xb9"


    encoded_args = b""
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



