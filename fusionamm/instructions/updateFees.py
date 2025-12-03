import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS

class UpdateFeesAccounts(typing.TypedDict):
    fusionPool:SolPubkey
    position:SolPubkey
    tickArrayLower:SolPubkey
    tickArrayUpper:SolPubkey

def UpdateFees(
    accounts: UpdateFeesAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["fusionPool"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["position"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tickArrayLower"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tickArrayUpper"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xe1\x1b\x0d\x06\x45\x54\xac\xbf"


    encoded_args = b""
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



