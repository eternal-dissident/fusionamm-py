import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS

class CloseLimitOrderAccounts(typing.TypedDict):
    limitOrderAuthority:SolPubkey
    receiver:SolPubkey
    limitOrder:SolPubkey
    limitOrderMint:SolPubkey
    limitOrderTokenAccount:SolPubkey
    token2022Program:SolPubkey

def CloseLimitOrder(
    accounts: CloseLimitOrderAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["limitOrderAuthority"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["receiver"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["limitOrder"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["limitOrderMint"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["limitOrderTokenAccount"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["token2022Program"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x4c\x7c\x80\x0f\xd5\x57\x25\xfa"


    encoded_args = b""
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



