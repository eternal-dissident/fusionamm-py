import borsh_construct as borsh
import typing
from construct import Construct, Container
from dataclasses import dataclass
from . import remainingAccountsSlice

class RemainingAccountsInfoJSON(typing.TypedDict):
    slices: list[remainingAccountsSlice.RemainingAccountsSliceJSON]

@dataclass
class RemainingAccountsInfo:
    layout: typing.ClassVar = borsh.CStruct(
        "slices" /borsh.Vec(typing.cast(Construct, remainingAccountsSlice.RemainingAccountsSlice.layout)),
        )
    #fields
    slices: list[remainingAccountsSlice.RemainingAccountsSlice]
    
    @classmethod
    def from_decoded(cls, obj: Container) -> "RemainingAccountsInfo":
        return cls(
        slices=list(map(lambda item:remainingAccountsSlice.RemainingAccountsSlice.from_json(item),obj["slices"])),
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
                "slices": list(map(lambda item:item.to_encodable(),self.slices)),
                }

    def to_json(self) -> RemainingAccountsInfoJSON:
        return {
                "slices": list(map(lambda item:item.to_json(),self.slices)),
                }

    @classmethod
    def from_json(cls, obj: RemainingAccountsInfoJSON) -> "RemainingAccountsInfo":
        return cls(
                slices=list(map(lambda item:remainingAccountsSlice.RemainingAccountsSlice.from_json(item),obj["slices"])),
        )






