import borsh_construct as borsh
import typing
from construct import Container
from dataclasses import dataclass

class TickJSON(typing.TypedDict):
    initialized: bool
    liquidityNet: int
    liquidityGross: int
    feeGrowthOutsideA: int
    feeGrowthOutsideB: int
    age: int
    openOrdersInput: int
    partFilledOrdersInput: int
    partFilledOrdersRemainingInput: int
    fulfilledAToBOrdersInput: int
    fulfilledBToAOrdersInput: int

@dataclass
class Tick:
    layout: typing.ClassVar = borsh.CStruct(
        "initialized" /borsh.Bool,
        "liquidityNet" /borsh.I128,
        "liquidityGross" /borsh.U128,
        "feeGrowthOutsideA" /borsh.U128,
        "feeGrowthOutsideB" /borsh.U128,
        "age" /borsh.U64,
        "openOrdersInput" /borsh.U64,
        "partFilledOrdersInput" /borsh.U64,
        "partFilledOrdersRemainingInput" /borsh.U64,
        "fulfilledAToBOrdersInput" /borsh.U64,
        "fulfilledBToAOrdersInput" /borsh.U64,
        )
    #fields
    initialized: bool
    liquidityNet: int
    liquidityGross: int
    feeGrowthOutsideA: int
    feeGrowthOutsideB: int
    age: int
    openOrdersInput: int
    partFilledOrdersInput: int
    partFilledOrdersRemainingInput: int
    fulfilledAToBOrdersInput: int
    fulfilledBToAOrdersInput: int
    
    @classmethod
    def from_decoded(cls, obj: Container) -> "Tick":
        return cls(
        initialized=obj["initialized"],
        liquidityNet=obj["liquidityNet"],
        liquidityGross=obj["liquidityGross"],
        feeGrowthOutsideA=obj["feeGrowthOutsideA"],
        feeGrowthOutsideB=obj["feeGrowthOutsideB"],
        age=obj["age"],
        openOrdersInput=obj["openOrdersInput"],
        partFilledOrdersInput=obj["partFilledOrdersInput"],
        partFilledOrdersRemainingInput=obj["partFilledOrdersRemainingInput"],
        fulfilledAToBOrdersInput=obj["fulfilledAToBOrdersInput"],
        fulfilledBToAOrdersInput=obj["fulfilledBToAOrdersInput"],
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
                "initialized": self.initialized,
                "liquidityNet": self.liquidityNet,
                "liquidityGross": self.liquidityGross,
                "feeGrowthOutsideA": self.feeGrowthOutsideA,
                "feeGrowthOutsideB": self.feeGrowthOutsideB,
                "age": self.age,
                "openOrdersInput": self.openOrdersInput,
                "partFilledOrdersInput": self.partFilledOrdersInput,
                "partFilledOrdersRemainingInput": self.partFilledOrdersRemainingInput,
                "fulfilledAToBOrdersInput": self.fulfilledAToBOrdersInput,
                "fulfilledBToAOrdersInput": self.fulfilledBToAOrdersInput,
                }

    def to_json(self) -> TickJSON:
        return {
                "initialized": self.initialized,
                "liquidityNet": self.liquidityNet,
                "liquidityGross": self.liquidityGross,
                "feeGrowthOutsideA": self.feeGrowthOutsideA,
                "feeGrowthOutsideB": self.feeGrowthOutsideB,
                "age": self.age,
                "openOrdersInput": self.openOrdersInput,
                "partFilledOrdersInput": self.partFilledOrdersInput,
                "partFilledOrdersRemainingInput": self.partFilledOrdersRemainingInput,
                "fulfilledAToBOrdersInput": self.fulfilledAToBOrdersInput,
                "fulfilledBToAOrdersInput": self.fulfilledBToAOrdersInput,
                }

    @classmethod
    def from_json(cls, obj: TickJSON) -> "Tick":
        return cls(
                initialized=obj["initialized"],
                liquidityNet=obj["liquidityNet"],
                liquidityGross=obj["liquidityGross"],
                feeGrowthOutsideA=obj["feeGrowthOutsideA"],
                feeGrowthOutsideB=obj["feeGrowthOutsideB"],
                age=obj["age"],
                openOrdersInput=obj["openOrdersInput"],
                partFilledOrdersInput=obj["partFilledOrdersInput"],
                partFilledOrdersRemainingInput=obj["partFilledOrdersRemainingInput"],
                fulfilledAToBOrdersInput=obj["fulfilledAToBOrdersInput"],
                fulfilledBToAOrdersInput=obj["fulfilledBToAOrdersInput"],
        )






