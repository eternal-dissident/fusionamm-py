import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS

class SetCollectProtocolFeesAuthorityAccounts(typing.TypedDict):
    fusionPoolsConfig:SolPubkey
    collectProtocolFeesAuthority:SolPubkey
    newCollectProtocolFeesAuthority:SolPubkey

def SetCollectProtocolFeesAuthority(
    accounts: SetCollectProtocolFeesAuthorityAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["fusionPoolsConfig"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["collectProtocolFeesAuthority"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["newCollectProtocolFeesAuthority"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x22\x96\x5d\xf4\x8b\xe1\xe9\x43"


    encoded_args = b""
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



