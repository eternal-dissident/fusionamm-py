import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS

class ClosePositionAccounts(typing.TypedDict):
    positionAuthority:SolPubkey
    receiver:SolPubkey
    position:SolPubkey
    positionMint:SolPubkey
    positionTokenAccount:SolPubkey
    token2022Program:SolPubkey

def ClosePosition(
    accounts: ClosePositionAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["positionAuthority"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["receiver"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["position"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["positionMint"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["positionTokenAccount"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["token2022Program"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x7b\x86\x51\x00\x31\x44\x62\x62"


    encoded_args = b""
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



