import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS

class SetTokenBadgeAuthorityAccounts(typing.TypedDict):
    fusionPoolsConfig:SolPubkey
    feeAuthority:SolPubkey
    newTokenBadgeAuthority:SolPubkey

def SetTokenBadgeAuthority(
    accounts: SetTokenBadgeAuthorityAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["fusionPoolsConfig"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["feeAuthority"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["newTokenBadgeAuthority"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xcf\xca\x04\x20\xcd\x4f\x0d\xb2"


    encoded_args = b""
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



