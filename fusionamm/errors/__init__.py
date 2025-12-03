import typing
import re
from solders.transaction_status import (
    InstructionErrorCustom,
    TransactionErrorInstructionError,
)
from solders.pubkey import Pubkey as SolPubkey
from solana.rpc.core import RPCException
from solders.rpc.errors import SendTransactionPreflightFailureMessage
from anchorpy.error import extract_code_and_logs

from . import fusionamm
from ..program_id import FUSIONAMM_PROGRAM_ADDRESS

error_re = re.compile(r"Program (\w+) failed: custom program error: (\w+)")

def from_tx_error(
    error: RPCException,
) -> typing.Union[.CustomError, None]:
    err_info = error.args[0]
    extracted = extract_code_and_logs(err_info, FUSIONAMM_PROGRAM_ADDRESS)
    if extracted is None:
        return None
    return fusionamm.from_code(extracted[0])
