import borsh_construct as borsh
import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from .. import types
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS
class IncreaseLimitOrderArgs(typing.TypedDict):
    amount:int
    remainingAccountsInfo:typing.Optional[types.remainingAccountsInfo.RemainingAccountsInfo]


layout = borsh.CStruct(
    "amount" /borsh.U64,
    "remainingAccountsInfo" /borsh.Option(types.remainingAccountsInfo.RemainingAccountsInfo.layout),
    )


class IncreaseLimitOrderAccounts(typing.TypedDict):
    limitOrderAuthority:SolPubkey
    fusionPool:SolPubkey
    limitOrder:SolPubkey
    limitOrderTokenAccount:SolPubkey
    tokenMint:SolPubkey
    tokenOwnerAccount:SolPubkey
    tokenVault:SolPubkey
    tickArray:SolPubkey
    tokenProgram:SolPubkey
    memoProgram:SolPubkey

def IncreaseLimitOrder(
    args: IncreaseLimitOrderArgs,
    accounts: IncreaseLimitOrderAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["limitOrderAuthority"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["fusionPool"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["limitOrder"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["limitOrderTokenAccount"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenMint"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenOwnerAccount"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenVault"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tickArray"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenProgram"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["memoProgram"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xb1\x90\x59\xec\xfa\xba\x7d\x63"


    encoded_args = layout.build({
        "amount":args["amount"],
        "remainingAccountsInfo":(None if args["remainingAccountsInfo"] is None else args["remainingAccountsInfo"].to_encodable()),
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)




