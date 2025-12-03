import borsh_construct as borsh
import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from .. import types
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS
class SwapArgs(typing.TypedDict):
    amount:int
    otherAmountThreshold:int
    sqrtPriceLimit:int
    amountSpecifiedIsInput:bool
    aToB:bool
    remainingAccountsInfo:typing.Optional[types.remainingAccountsInfo.RemainingAccountsInfo]


layout = borsh.CStruct(
    "amount" /borsh.U64,
    "otherAmountThreshold" /borsh.U64,
    "sqrtPriceLimit" /borsh.U128,
    "amountSpecifiedIsInput" /borsh.Bool,
    "aToB" /borsh.Bool,
    "remainingAccountsInfo" /borsh.Option(types.remainingAccountsInfo.RemainingAccountsInfo.layout),
    )


class SwapAccounts(typing.TypedDict):
    tokenProgramA:SolPubkey
    tokenProgramB:SolPubkey
    memoProgram:SolPubkey
    tokenAuthority:SolPubkey
    fusionPool:SolPubkey
    tokenMintA:SolPubkey
    tokenMintB:SolPubkey
    tokenOwnerAccountA:SolPubkey
    tokenOwnerAccountB:SolPubkey
    tokenVaultA:SolPubkey
    tokenVaultB:SolPubkey
    tickArray0:SolPubkey
    tickArray1:SolPubkey
    tickArray2:SolPubkey

def Swap(
    args: SwapArgs,
    accounts: SwapAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["tokenProgramA"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenProgramB"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["memoProgram"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenAuthority"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["fusionPool"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenMintA"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenMintB"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenOwnerAccountA"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenOwnerAccountB"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenVaultA"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenVaultB"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tickArray0"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tickArray1"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tickArray2"], is_signer=False, is_writable=True),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xf8\xc6\x9e\x91\xe1\x75\x87\xc8"


    encoded_args = layout.build({
        "amount":args["amount"],
        "otherAmountThreshold":args["otherAmountThreshold"],
        "sqrtPriceLimit":args["sqrtPriceLimit"],
        "amountSpecifiedIsInput":args["amountSpecifiedIsInput"],
        "aToB":args["aToB"],
        "remainingAccountsInfo":(None if args["remainingAccountsInfo"] is None else args["remainingAccountsInfo"].to_encodable()),
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



