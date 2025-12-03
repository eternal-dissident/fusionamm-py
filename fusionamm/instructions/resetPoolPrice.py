import borsh_construct as borsh
import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS
class ResetPoolPriceArgs(typing.TypedDict):
    sqrtPrice:int


layout = borsh.CStruct(
    "sqrtPrice" /borsh.U128,
    )


class ResetPoolPriceAccounts(typing.TypedDict):
    feeAuthority:SolPubkey
    fusionPoolsConfig:SolPubkey
    tokenVaultA:SolPubkey
    tokenVaultB:SolPubkey
    fusionPool:SolPubkey

def ResetPoolPrice(
    args: ResetPoolPriceArgs,
    accounts: ResetPoolPriceAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["feeAuthority"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["fusionPoolsConfig"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenVaultA"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenVaultB"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["fusionPool"], is_signer=False, is_writable=True),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x5d\x9e\x9e\xbd\x83\x2a\x0f\x16"


    encoded_args = layout.build({
        "sqrtPrice":args["sqrtPrice"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



