import borsh_construct as borsh
import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from .. import types
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS
class TwoHopSwapArgs(typing.TypedDict):
    amount:int
    otherAmountThreshold:int
    amountSpecifiedIsInput:bool
    aToBOne:bool
    aToBTwo:bool
    sqrtPriceLimitOne:int
    sqrtPriceLimitTwo:int
    remainingAccountsInfo:typing.Optional[types.remainingAccountsInfo.RemainingAccountsInfo]


layout = borsh.CStruct(
    "amount" /borsh.U64,
    "otherAmountThreshold" /borsh.U64,
    "amountSpecifiedIsInput" /borsh.Bool,
    "aToBOne" /borsh.Bool,
    "aToBTwo" /borsh.Bool,
    "sqrtPriceLimitOne" /borsh.U128,
    "sqrtPriceLimitTwo" /borsh.U128,
    "remainingAccountsInfo" /borsh.Option(types.remainingAccountsInfo.RemainingAccountsInfo.layout),
    )


class TwoHopSwapAccounts(typing.TypedDict):
    fusionPoolOne:SolPubkey
    fusionPoolTwo:SolPubkey
    tokenMintInput:SolPubkey
    tokenMintIntermediate:SolPubkey
    tokenMintOutput:SolPubkey
    tokenProgramInput:SolPubkey
    tokenProgramIntermediate:SolPubkey
    tokenProgramOutput:SolPubkey
    tokenOwnerAccountInput:SolPubkey
    tokenVaultOneInput:SolPubkey
    tokenVaultOneIntermediate:SolPubkey
    tokenVaultTwoIntermediate:SolPubkey
    tokenVaultTwoOutput:SolPubkey
    tokenOwnerAccountOutput:SolPubkey
    tokenAuthority:SolPubkey
    tickArrayOne0:SolPubkey
    tickArrayOne1:SolPubkey
    tickArrayOne2:SolPubkey
    tickArrayTwo0:SolPubkey
    tickArrayTwo1:SolPubkey
    tickArrayTwo2:SolPubkey
    memoProgram:SolPubkey

def TwoHopSwap(
    args: TwoHopSwapArgs,
    accounts: TwoHopSwapAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["fusionPoolOne"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["fusionPoolTwo"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenMintInput"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenMintIntermediate"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenMintOutput"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenProgramInput"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenProgramIntermediate"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenProgramOutput"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenOwnerAccountInput"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenVaultOneInput"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenVaultOneIntermediate"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenVaultTwoIntermediate"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenVaultTwoOutput"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenOwnerAccountOutput"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenAuthority"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["tickArrayOne0"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tickArrayOne1"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tickArrayOne2"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tickArrayTwo0"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tickArrayTwo1"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tickArrayTwo2"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["memoProgram"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xc3\x60\xed\x6c\x44\xa2\xdb\xe6"


    encoded_args = layout.build({
        "amount":args["amount"],
        "otherAmountThreshold":args["otherAmountThreshold"],
        "amountSpecifiedIsInput":args["amountSpecifiedIsInput"],
        "aToBOne":args["aToBOne"],
        "aToBTwo":args["aToBTwo"],
        "sqrtPriceLimitOne":args["sqrtPriceLimitOne"],
        "sqrtPriceLimitTwo":args["sqrtPriceLimitTwo"],
        "remainingAccountsInfo":(None if args["remainingAccountsInfo"] is None else args["remainingAccountsInfo"].to_encodable()),
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



