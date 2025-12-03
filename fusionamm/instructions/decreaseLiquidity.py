import borsh_construct as borsh
import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from .. import types
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS
class DecreaseLiquidityArgs(typing.TypedDict):
    liquidityAmount:int
    tokenMinA:int
    tokenMinB:int
    remainingAccountsInfo:typing.Optional[types.remainingAccountsInfo.RemainingAccountsInfo]


layout = borsh.CStruct(
    "liquidityAmount" /borsh.U128,
    "tokenMinA" /borsh.U64,
    "tokenMinB" /borsh.U64,
    "remainingAccountsInfo" /borsh.Option(types.remainingAccountsInfo.RemainingAccountsInfo.layout),
    )


class DecreaseLiquidityAccounts(typing.TypedDict):
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

def DecreaseLiquidity(
    args: DecreaseLiquidityArgs,
    accounts: DecreaseLiquidityAccounts,
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
    identifier = b"\xa0\x26\xd0\x6f\x68\x5b\x2c\x01"


    encoded_args = layout.build({
        "liquidityAmount":args["liquidityAmount"],
        "tokenMinA":args["tokenMinA"],
        "tokenMinB":args["tokenMinB"],
        "remainingAccountsInfo":(None if args["remainingAccountsInfo"] is None else args["remainingAccountsInfo"].to_encodable()),
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



