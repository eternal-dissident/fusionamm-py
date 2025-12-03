import borsh_construct as borsh
import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS
class OpenPositionArgs(typing.TypedDict):
    tickLowerIndex:int
    tickUpperIndex:int
    withTokenMetadataExtension:bool


layout = borsh.CStruct(
    "tickLowerIndex" /borsh.I32,
    "tickUpperIndex" /borsh.I32,
    "withTokenMetadataExtension" /borsh.Bool,
    )


class OpenPositionAccounts(typing.TypedDict):
    funder:SolPubkey
    owner:SolPubkey
    position:SolPubkey
    positionMint:SolPubkey
    positionTokenAccount:SolPubkey
    fusionPool:SolPubkey
    token2022Program:SolPubkey
    systemProgram:SolPubkey
    associatedTokenProgram:SolPubkey
    metadataUpdateAuth:SolPubkey

def OpenPosition(
    args: OpenPositionArgs,
    accounts: OpenPositionAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["funder"], is_signer=True, is_writable=True),
    AccountMeta(pubkey=accounts["owner"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["position"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["positionMint"], is_signer=True, is_writable=True),
    AccountMeta(pubkey=accounts["positionTokenAccount"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["fusionPool"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["token2022Program"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["systemProgram"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["associatedTokenProgram"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["metadataUpdateAuth"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x87\x80\x2f\x4d\x0f\x98\xf0\x31"


    encoded_args = layout.build({
        "tickLowerIndex":args["tickLowerIndex"],
        "tickUpperIndex":args["tickUpperIndex"],
        "withTokenMetadataExtension":args["withTokenMetadataExtension"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)




