import borsh_construct as borsh
import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from .. import types
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS
class IncreaseLiquidityArgs(typing.TypedDict):
    liquidityAmount:int
    tokenMaxA:int
    tokenMaxB:int
    remainingAccountsInfo:typing.Optional[types.remainingAccountsInfo.RemainingAccountsInfo]


layout = borsh.CStruct(
    "liquidityAmount" /borsh.U128,
    "tokenMaxA" /borsh.U64,
    "tokenMaxB" /borsh.U64,
    "remainingAccountsInfo" /borsh.Option(types.remainingAccountsInfo.RemainingAccountsInfo.layout),
    )


class IncreaseLiquidityAccounts(typing.TypedDict):
    fusionPool:SolPubkey
    tokenProgramA:SolPubkey
    tokenProgramB:SolPubkey
    memoProgram:SolPubkey
    positionAuthority:SolPubkey
    position:SolPubkey
    positionTokenAccount:SolPubkey
    tokenMintA:SolPubkey
    tokenMintB:SolPubkey
    tokenOwnerAccountA:SolPubkey
    tokenOwnerAccountB:SolPubkey
    tokenVaultA:SolPubkey
    tokenVaultB:SolPubkey
    tickArrayLower:SolPubkey
    tickArrayUpper:SolPubkey

def IncreaseLiquidity(
    args: IncreaseLiquidityArgs,
    accounts: IncreaseLiquidityAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["fusionPool"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenProgramA"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenProgramB"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["memoProgram"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["positionAuthority"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["position"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["positionTokenAccount"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenMintA"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenMintB"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenOwnerAccountA"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenOwnerAccountB"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenVaultA"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenVaultB"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tickArrayLower"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tickArrayUpper"], is_signer=False, is_writable=True),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x2e\x9c\xf3\x76\x0d\xcd\xfb\xb2"


    encoded_args = layout.build({
        "liquidityAmount":args["liquidityAmount"],
        "tokenMaxA":args["tokenMaxA"],
        "tokenMaxB":args["tokenMaxB"],
        "remainingAccountsInfo":(None if args["remainingAccountsInfo"] is None else args["remainingAccountsInfo"].to_encodable()),
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



