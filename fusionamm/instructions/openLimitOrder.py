import borsh_construct as borsh
import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS
class OpenLimitOrderArgs(typing.TypedDict):
    tickIndex:int
    aToB:bool
    withTokenMetadataExtension:bool


layout = borsh.CStruct(
    "tickIndex" /borsh.I32,
    "aToB" /borsh.Bool,
    "withTokenMetadataExtension" /borsh.Bool,
    )


class OpenLimitOrderAccounts(typing.TypedDict):
    funder:SolPubkey
    owner:SolPubkey
    limitOrder:SolPubkey
    limitOrderMint:SolPubkey
    limitOrderTokenAccount:SolPubkey
    fusionPool:SolPubkey
    token2022Program:SolPubkey
    systemProgram:SolPubkey
    associatedTokenProgram:SolPubkey
    metadataUpdateAuth:SolPubkey

def OpenLimitOrder(
    args: OpenLimitOrderArgs,
    accounts: OpenLimitOrderAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["funder"], is_signer=True, is_writable=True),
    AccountMeta(pubkey=accounts["owner"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["limitOrder"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["limitOrderMint"], is_signer=True, is_writable=True),
    AccountMeta(pubkey=accounts["limitOrderTokenAccount"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["fusionPool"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["token2022Program"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["systemProgram"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["associatedTokenProgram"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["metadataUpdateAuth"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x9d\x20\xda\xb7\x47\x1d\x12\x93"


    encoded_args = layout.build({
        "tickIndex":args["tickIndex"],
        "aToB":args["aToB"],
        "withTokenMetadataExtension":args["withTokenMetadataExtension"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)




