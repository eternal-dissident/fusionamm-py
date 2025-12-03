import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS

class SetFeeAuthorityAccounts(typing.TypedDict):
    fusionPoolsConfig:SolPubkey
    feeAuthority:SolPubkey
    newFeeAuthority:SolPubkey

def SetFeeAuthority(
    accounts: SetFeeAuthorityAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["fusionPoolsConfig"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["feeAuthority"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["newFeeAuthority"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x1f\x01\x32\x57\xed\x65\x61\x84"


    encoded_args = b""
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



