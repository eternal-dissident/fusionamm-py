import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS

class InitializePositionBundleWithMetadataAccounts(typing.TypedDict):
    positionBundle:SolPubkey
    positionBundleMint:SolPubkey
    positionBundleMetadata:SolPubkey
    positionBundleTokenAccount:SolPubkey
    positionBundleOwner:SolPubkey
    funder:SolPubkey
    metadataUpdateAuth:SolPubkey
    tokenProgram:SolPubkey
    systemProgram:SolPubkey
    rent:SolPubkey
    associatedTokenProgram:SolPubkey
    metadataProgram:SolPubkey

def InitializePositionBundleWithMetadata(
    accounts: InitializePositionBundleWithMetadataAccounts,
    program_id: SolPubkey =  FUSIONAMM_PROGRAM_ADDRESS,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["positionBundle"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["positionBundleMint"], is_signer=True, is_writable=True),
    AccountMeta(pubkey=accounts["positionBundleMetadata"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["positionBundleTokenAccount"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["positionBundleOwner"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["funder"], is_signer=True, is_writable=True),
    AccountMeta(pubkey=accounts["metadataUpdateAuth"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenProgram"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["systemProgram"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["associatedTokenProgram"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["metadataProgram"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x5d\x7c\x10\xb3\xf9\x83\x73\xf5"


    encoded_args = b""
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)








