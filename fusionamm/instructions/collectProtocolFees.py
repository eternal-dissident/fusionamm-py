import borsh_construct as borsh
import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from .. import types
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS
class CollectProtocolFeesArgs(typing.TypedDict):
    remainingAccountsInfo:typing.Optional[types.remainingAccountsInfo.RemainingAccountsInfo]


layout = borsh.CStruct(
    "remainingAccountsInfo" /borsh.Option(types.remainingAccountsInfo.RemainingAccountsInfo.layout),
    )


class CollectProtocolFeesAccounts(typing.TypedDict):
    fusionPoolsConfig:SolPubkey
    fusionPool:SolPubkey
    collectProtocolFeesAuthority:SolPubkey
    tokenMintA:SolPubkey
    tokenMintB:SolPubkey
    tokenVaultA:SolPubkey
    tokenVaultB:SolPubkey
    tokenDestinationA:SolPubkey
    tokenDestinationB:SolPubkey
    tokenProgramA:SolPubkey
    tokenProgramB:SolPubkey
    memoProgram:SolPubkey

def CollectProtocolFees(
    args: CollectProtocolFeesArgs,
    accounts: CollectProtocolFeesAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["fusionPoolsConfig"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["fusionPool"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["collectProtocolFeesAuthority"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["tokenMintA"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenMintB"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenVaultA"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenVaultB"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenDestinationA"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenDestinationB"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenProgramA"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenProgramB"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["memoProgram"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x16\x43\x17\x62\x96\xb2\x46\xdc"


    encoded_args = layout.build({
        "remainingAccountsInfo":(None if args["remainingAccountsInfo"] is None else args["remainingAccountsInfo"].to_encodable()),
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



