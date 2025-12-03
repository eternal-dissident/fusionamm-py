import borsh_construct as borsh
import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS
class InitializePoolArgs(typing.TypedDict):
    tickSpacing:int
    feeRate:int
    initialSqrtPrice:int


layout = borsh.CStruct(
    "tickSpacing" /borsh.U16,
    "feeRate" /borsh.U16,
    "initialSqrtPrice" /borsh.U128,
    )


class InitializePoolAccounts(typing.TypedDict):
    fusionPoolsConfig:SolPubkey
    tokenMintA:SolPubkey
    tokenMintB:SolPubkey
    tokenBadgeA:SolPubkey
    tokenBadgeB:SolPubkey
    funder:SolPubkey
    fusionPool:SolPubkey
    tokenVaultA:SolPubkey
    tokenVaultB:SolPubkey
    tokenProgramA:SolPubkey
    tokenProgramB:SolPubkey
    systemProgram:SolPubkey
    rent:SolPubkey

def InitializePool(
    args: InitializePoolArgs,
    accounts: InitializePoolAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["fusionPoolsConfig"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenMintA"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenMintB"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenBadgeA"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenBadgeB"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["funder"], is_signer=True, is_writable=True),
    AccountMeta(pubkey=accounts["fusionPool"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenVaultA"], is_signer=True, is_writable=True),
    AccountMeta(pubkey=accounts["tokenVaultB"], is_signer=True, is_writable=True),
    AccountMeta(pubkey=accounts["tokenProgramA"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenProgramB"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["systemProgram"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x5f\xb4\x0a\xac\x54\xae\xe8\x28"


    encoded_args = layout.build({
        "tickSpacing":args["tickSpacing"],
        "feeRate":args["feeRate"],
        "initialSqrtPrice":args["initialSqrtPrice"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)






