import borsh_construct as borsh
import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS
class InitializeTickArrayArgs(typing.TypedDict):
    startTickIndex:int


layout = borsh.CStruct(
    "startTickIndex" /borsh.I32,
    )


class InitializeTickArrayAccounts(typing.TypedDict):
    fusionPool:SolPubkey
    funder:SolPubkey
    tickArray:SolPubkey
    systemProgram:SolPubkey

def InitializeTickArray(
    args: InitializeTickArrayArgs,
    accounts: InitializeTickArrayAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["fusionPool"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["funder"], is_signer=True, is_writable=True),
    AccountMeta(pubkey=accounts["tickArray"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["systemProgram"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x0b\xbc\xc1\xd6\x8d\x5b\x95\xb8"


    encoded_args = layout.build({
        "startTickIndex":args["startTickIndex"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)




