import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS

class InitializeTokenBadgeAccounts(typing.TypedDict):
    fusionPoolsConfig:SolPubkey
    tokenBadgeAuthority:SolPubkey
    tokenMint:SolPubkey
    tokenBadge:SolPubkey
    funder:SolPubkey
    systemProgram:SolPubkey

def InitializeTokenBadge(
    accounts: InitializeTokenBadgeAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["fusionPoolsConfig"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenBadgeAuthority"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["tokenMint"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenBadge"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["funder"], is_signer=True, is_writable=True),
    AccountMeta(pubkey=accounts["systemProgram"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xfd\x4d\xcd\x5f\x1b\xe0\x59\xdf"


    encoded_args = b""
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)




