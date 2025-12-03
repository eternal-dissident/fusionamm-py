import borsh_construct as borsh
import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS
class OpenBundledPositionArgs(typing.TypedDict):
    bundleIndex:int
    tickLowerIndex:int
    tickUpperIndex:int


layout = borsh.CStruct(
    "bundleIndex" /borsh.U16,
    "tickLowerIndex" /borsh.I32,
    "tickUpperIndex" /borsh.I32,
    )


class OpenBundledPositionAccounts(typing.TypedDict):
    bundledPosition:SolPubkey
    positionBundle:SolPubkey
    positionBundleTokenAccount:SolPubkey
    positionBundleAuthority:SolPubkey
    fusionPool:SolPubkey
    funder:SolPubkey
    systemProgram:SolPubkey
    rent:SolPubkey

def OpenBundledPosition(
    args: OpenBundledPositionArgs,
    accounts: OpenBundledPositionAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["bundledPosition"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["positionBundle"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["positionBundleTokenAccount"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["positionBundleAuthority"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["fusionPool"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["funder"], is_signer=True, is_writable=True),
    AccountMeta(pubkey=accounts["systemProgram"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xa9\x71\x7e\xab\xd5\xac\xd4\x31"


    encoded_args = layout.build({
        "bundleIndex":args["bundleIndex"],
        "tickLowerIndex":args["tickLowerIndex"],
        "tickUpperIndex":args["tickUpperIndex"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)






