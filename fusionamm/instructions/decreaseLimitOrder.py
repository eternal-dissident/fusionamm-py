import borsh_construct as borsh
import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from .. import types
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS
class DecreaseLimitOrderArgs(typing.TypedDict):
    amount:int
    remainingAccountsInfo:typing.Optional[types.remainingAccountsInfo.RemainingAccountsInfo]


layout = borsh.CStruct(
    "amount" /borsh.U64,
    "remainingAccountsInfo" /borsh.Option(types.remainingAccountsInfo.RemainingAccountsInfo.layout),
    )


class DecreaseLimitOrderAccounts(typing.TypedDict):
    limitOrderAuthority:SolPubkey
    fusionPool:SolPubkey
    limitOrder:SolPubkey
    limitOrderTokenAccount:SolPubkey
    tokenMintA:SolPubkey
    tokenMintB:SolPubkey
    tokenOwnerAccountA:SolPubkey
    tokenOwnerAccountB:SolPubkey
    tokenVaultA:SolPubkey
    tokenVaultB:SolPubkey
    tickArray:SolPubkey
    tokenProgramA:SolPubkey
    tokenProgramB:SolPubkey
    memoProgram:SolPubkey

def DecreaseLimitOrder(
    args: DecreaseLimitOrderArgs,
    accounts: DecreaseLimitOrderAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["limitOrderAuthority"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["fusionPool"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["limitOrder"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["limitOrderTokenAccount"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenMintA"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenMintB"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenOwnerAccountA"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenOwnerAccountB"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenVaultA"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenVaultB"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tickArray"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenProgramA"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenProgramB"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["memoProgram"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x75\x9d\x3c\x67\x42\x31\xa3\x00"


    encoded_args = layout.build({
        "amount":args["amount"],
        "remainingAccountsInfo":(None if args["remainingAccountsInfo"] is None else args["remainingAccountsInfo"].to_encodable()),
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



