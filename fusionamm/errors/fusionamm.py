import typing
from anchorpy.error import ProgramError

class InvalidEnum(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6000, ""
        )

    code = 6000
    name = "InvalidEnum"
    msg = ""
class InvalidStartTick(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6001, ""
        )

    code = 6001
    name = "InvalidStartTick"
    msg = ""
class TickArrayExistInPool(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6002, ""
        )

    code = 6002
    name = "TickArrayExistInPool"
    msg = ""
class TickArrayIndexOutofBounds(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6003, ""
        )

    code = 6003
    name = "TickArrayIndexOutofBounds"
    msg = ""
class InvalidTickSpacing(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6004, ""
        )

    code = 6004
    name = "InvalidTickSpacing"
    msg = ""
class ClosePositionNotEmpty(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6005, ""
        )

    code = 6005
    name = "ClosePositionNotEmpty"
    msg = ""
class DivideByZero(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6006, ""
        )

    code = 6006
    name = "DivideByZero"
    msg = ""
class NumberCastError(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6007, ""
        )

    code = 6007
    name = "NumberCastError"
    msg = ""
class NumberDownCastError(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6008, ""
        )

    code = 6008
    name = "NumberDownCastError"
    msg = ""
class TickNotFound(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6009, ""
        )

    code = 6009
    name = "TickNotFound"
    msg = ""
class InvalidTickIndex(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6010, ""
        )

    code = 6010
    name = "InvalidTickIndex"
    msg = ""
class SqrtPriceOutOfBounds(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6011, ""
        )

    code = 6011
    name = "SqrtPriceOutOfBounds"
    msg = ""
class LiquidityZero(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6012, ""
        )

    code = 6012
    name = "LiquidityZero"
    msg = ""
class LiquidityTooHigh(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6013, ""
        )

    code = 6013
    name = "LiquidityTooHigh"
    msg = ""
class LiquidityOverflow(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6014, ""
        )

    code = 6014
    name = "LiquidityOverflow"
    msg = ""
class LiquidityUnderflow(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6015, ""
        )

    code = 6015
    name = "LiquidityUnderflow"
    msg = ""
class LiquidityNetError(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6016, ""
        )

    code = 6016
    name = "LiquidityNetError"
    msg = ""
class TokenMaxExceeded(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6017, ""
        )

    code = 6017
    name = "TokenMaxExceeded"
    msg = ""
class TokenMinSubceeded(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6018, ""
        )

    code = 6018
    name = "TokenMinSubceeded"
    msg = ""
class MissingOrInvalidDelegate(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6019, ""
        )

    code = 6019
    name = "MissingOrInvalidDelegate"
    msg = ""
class InvalidPositionTokenAmount(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6020, ""
        )

    code = 6020
    name = "InvalidPositionTokenAmount"
    msg = ""
class InvalidTimestampConversion(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6021, ""
        )

    code = 6021
    name = "InvalidTimestampConversion"
    msg = ""
class InvalidTimestamp(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6022, ""
        )

    code = 6022
    name = "InvalidTimestamp"
    msg = ""
class InvalidTickArraySequence(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6023, ""
        )

    code = 6023
    name = "InvalidTickArraySequence"
    msg = ""
class InvalidTokenMintOrder(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6024, ""
        )

    code = 6024
    name = "InvalidTokenMintOrder"
    msg = ""
class SetRangeForNonEmptyPosition(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6025, ""
        )

    code = 6025
    name = "SetRangeForNonEmptyPosition"
    msg = ""
class Unused(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6026, ""
        )

    code = 6026
    name = "Unused"
    msg = ""
class RewardVaultAmountInsufficient(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6027, ""
        )

    code = 6027
    name = "RewardVaultAmountInsufficient"
    msg = ""
class FeeRateMaxExceeded(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6028, ""
        )

    code = 6028
    name = "FeeRateMaxExceeded"
    msg = ""
class ProtocolFeeRateMaxExceeded(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6029, ""
        )

    code = 6029
    name = "ProtocolFeeRateMaxExceeded"
    msg = ""
class MultiplicationShiftRightOverflow(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6030, ""
        )

    code = 6030
    name = "MultiplicationShiftRightOverflow"
    msg = ""
class MulDivOverflow(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6031, ""
        )

    code = 6031
    name = "MulDivOverflow"
    msg = ""
class MulDivInvalidInput(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6032, ""
        )

    code = 6032
    name = "MulDivInvalidInput"
    msg = ""
class MultiplicationOverflow(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6033, ""
        )

    code = 6033
    name = "MultiplicationOverflow"
    msg = ""
class InvalidSqrtPriceLimitDirection(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6034, ""
        )

    code = 6034
    name = "InvalidSqrtPriceLimitDirection"
    msg = ""
class ZeroTradableAmount(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6035, ""
        )

    code = 6035
    name = "ZeroTradableAmount"
    msg = ""
class AmountOutBelowMinimum(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6036, ""
        )

    code = 6036
    name = "AmountOutBelowMinimum"
    msg = ""
class AmountInAboveMaximum(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6037, ""
        )

    code = 6037
    name = "AmountInAboveMaximum"
    msg = ""
class TickArraySequenceInvalidIndex(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6038, ""
        )

    code = 6038
    name = "TickArraySequenceInvalidIndex"
    msg = ""
class AmountCalcOverflow(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6039, ""
        )

    code = 6039
    name = "AmountCalcOverflow"
    msg = ""
class AmountRemainingOverflow(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6040, ""
        )

    code = 6040
    name = "AmountRemainingOverflow"
    msg = ""
class InvalidIntermediaryMint(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6041, ""
        )

    code = 6041
    name = "InvalidIntermediaryMint"
    msg = ""
class DuplicateTwoHopPool(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6042, ""
        )

    code = 6042
    name = "DuplicateTwoHopPool"
    msg = ""
class InvalidBundleIndex(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6043, ""
        )

    code = 6043
    name = "InvalidBundleIndex"
    msg = ""
class BundledPositionAlreadyOpened(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6044, ""
        )

    code = 6044
    name = "BundledPositionAlreadyOpened"
    msg = ""
class BundledPositionAlreadyClosed(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6045, ""
        )

    code = 6045
    name = "BundledPositionAlreadyClosed"
    msg = ""
class PositionBundleNotDeletable(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6046, ""
        )

    code = 6046
    name = "PositionBundleNotDeletable"
    msg = ""
class UnsupportedTokenMint(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6047, ""
        )

    code = 6047
    name = "UnsupportedTokenMint"
    msg = ""
class RemainingAccountsInvalidSlice(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6048, ""
        )

    code = 6048
    name = "RemainingAccountsInvalidSlice"
    msg = ""
class RemainingAccountsInsufficient(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6049, ""
        )

    code = 6049
    name = "RemainingAccountsInsufficient"
    msg = ""
class NoExtraAccountsForTransferHook(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6050, ""
        )

    code = 6050
    name = "NoExtraAccountsForTransferHook"
    msg = ""
class IntermediateTokenAmountMismatch(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6051, ""
        )

    code = 6051
    name = "IntermediateTokenAmountMismatch"
    msg = ""
class TransferFeeCalculationError(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6052, ""
        )

    code = 6052
    name = "TransferFeeCalculationError"
    msg = ""
class RemainingAccountsDuplicatedAccountsType(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6053, ""
        )

    code = 6053
    name = "RemainingAccountsDuplicatedAccountsType"
    msg = ""
class FullRangeOnlyPool(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6054, ""
        )

    code = 6054
    name = "FullRangeOnlyPool"
    msg = ""
class TooManySupplementalTickArrays(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6055, ""
        )

    code = 6055
    name = "TooManySupplementalTickArrays"
    msg = ""
class DifferentFusionPoolTickArrayAccount(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6056, ""
        )

    code = 6056
    name = "DifferentFusionPoolTickArrayAccount"
    msg = ""
class PartialFillError(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6057, ""
        )

    code = 6057
    name = "PartialFillError"
    msg = ""
class TakerOrderNotSupported(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6058, ""
        )

    code = 6058
    name = "TakerOrderNotSupported"
    msg = ""
class LimitOrderAmountExceeded(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6059, ""
        )

    code = 6059
    name = "LimitOrderAmountExceeded"
    msg = ""
class LimitOrderNotEmpty(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6060, ""
        )

    code = 6060
    name = "LimitOrderNotEmpty"
    msg = ""
class LimitOrderIsFilled(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6061, ""
        )

    code = 6061
    name = "LimitOrderIsFilled"
    msg = ""
class ZeroAmount(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6062, ""
        )

    code = 6062
    name = "ZeroAmount"
    msg = ""
class ResetPriceForNonEmptyPool(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6063, ""
        )

    code = 6063
    name = "ResetPriceForNonEmptyPool"
    msg = ""

CustomError = typing.Union[
    InvalidEnum,
    InvalidStartTick,
    TickArrayExistInPool,
    TickArrayIndexOutofBounds,
    InvalidTickSpacing,
    ClosePositionNotEmpty,
    DivideByZero,
    NumberCastError,
    NumberDownCastError,
    TickNotFound,
    InvalidTickIndex,
    SqrtPriceOutOfBounds,
    LiquidityZero,
    LiquidityTooHigh,
    LiquidityOverflow,
    LiquidityUnderflow,
    LiquidityNetError,
    TokenMaxExceeded,
    TokenMinSubceeded,
    MissingOrInvalidDelegate,
    InvalidPositionTokenAmount,
    InvalidTimestampConversion,
    InvalidTimestamp,
    InvalidTickArraySequence,
    InvalidTokenMintOrder,
    SetRangeForNonEmptyPosition,
    Unused,
    RewardVaultAmountInsufficient,
    FeeRateMaxExceeded,
    ProtocolFeeRateMaxExceeded,
    MultiplicationShiftRightOverflow,
    MulDivOverflow,
    MulDivInvalidInput,
    MultiplicationOverflow,
    InvalidSqrtPriceLimitDirection,
    ZeroTradableAmount,
    AmountOutBelowMinimum,
    AmountInAboveMaximum,
    TickArraySequenceInvalidIndex,
    AmountCalcOverflow,
    AmountRemainingOverflow,
    InvalidIntermediaryMint,
    DuplicateTwoHopPool,
    InvalidBundleIndex,
    BundledPositionAlreadyOpened,
    BundledPositionAlreadyClosed,
    PositionBundleNotDeletable,
    UnsupportedTokenMint,
    RemainingAccountsInvalidSlice,
    RemainingAccountsInsufficient,
    NoExtraAccountsForTransferHook,
    IntermediateTokenAmountMismatch,
    TransferFeeCalculationError,
    RemainingAccountsDuplicatedAccountsType,
    FullRangeOnlyPool,
    TooManySupplementalTickArrays,
    DifferentFusionPoolTickArrayAccount,
    PartialFillError,
    TakerOrderNotSupported,
    LimitOrderAmountExceeded,
    LimitOrderNotEmpty,
    LimitOrderIsFilled,
    ZeroAmount,
    ResetPriceForNonEmptyPool,
 ]
CUSTOM_ERROR_MAP: dict[int, CustomError] = {
    6000: InvalidEnum(),
    6001: InvalidStartTick(),
    6002: TickArrayExistInPool(),
    6003: TickArrayIndexOutofBounds(),
    6004: InvalidTickSpacing(),
    6005: ClosePositionNotEmpty(),
    6006: DivideByZero(),
    6007: NumberCastError(),
    6008: NumberDownCastError(),
    6009: TickNotFound(),
    6010: InvalidTickIndex(),
    6011: SqrtPriceOutOfBounds(),
    6012: LiquidityZero(),
    6013: LiquidityTooHigh(),
    6014: LiquidityOverflow(),
    6015: LiquidityUnderflow(),
    6016: LiquidityNetError(),
    6017: TokenMaxExceeded(),
    6018: TokenMinSubceeded(),
    6019: MissingOrInvalidDelegate(),
    6020: InvalidPositionTokenAmount(),
    6021: InvalidTimestampConversion(),
    6022: InvalidTimestamp(),
    6023: InvalidTickArraySequence(),
    6024: InvalidTokenMintOrder(),
    6025: SetRangeForNonEmptyPosition(),
    6026: Unused(),
    6027: RewardVaultAmountInsufficient(),
    6028: FeeRateMaxExceeded(),
    6029: ProtocolFeeRateMaxExceeded(),
    6030: MultiplicationShiftRightOverflow(),
    6031: MulDivOverflow(),
    6032: MulDivInvalidInput(),
    6033: MultiplicationOverflow(),
    6034: InvalidSqrtPriceLimitDirection(),
    6035: ZeroTradableAmount(),
    6036: AmountOutBelowMinimum(),
    6037: AmountInAboveMaximum(),
    6038: TickArraySequenceInvalidIndex(),
    6039: AmountCalcOverflow(),
    6040: AmountRemainingOverflow(),
    6041: InvalidIntermediaryMint(),
    6042: DuplicateTwoHopPool(),
    6043: InvalidBundleIndex(),
    6044: BundledPositionAlreadyOpened(),
    6045: BundledPositionAlreadyClosed(),
    6046: PositionBundleNotDeletable(),
    6047: UnsupportedTokenMint(),
    6048: RemainingAccountsInvalidSlice(),
    6049: RemainingAccountsInsufficient(),
    6050: NoExtraAccountsForTransferHook(),
    6051: IntermediateTokenAmountMismatch(),
    6052: TransferFeeCalculationError(),
    6053: RemainingAccountsDuplicatedAccountsType(),
    6054: FullRangeOnlyPool(),
    6055: TooManySupplementalTickArrays(),
    6056: DifferentFusionPoolTickArrayAccount(),
    6057: PartialFillError(),
    6058: TakerOrderNotSupported(),
    6059: LimitOrderAmountExceeded(),
    6060: LimitOrderNotEmpty(),
    6061: LimitOrderIsFilled(),
    6062: ZeroAmount(),
    6063: ResetPriceForNonEmptyPool(),
}

def from_code(code: int) -> typing.Optional[CustomError]:
    maybe_err = CUSTOM_ERROR_MAP.get(code)
    if maybe_err is None:
        return None
    return maybe_err

