# Class Statement [Type 1]
class DummyClass1:
    def __init__(self, value: dict[str, any]):
        self.value = value

    def method_1(self):
        print(f"definitions.DummyClass1.method_1()")

# Dynamic Type Creation with type() [Type 2]
def dynamic_type_init_1(self, value: dict[str, any]):
    self.value = value

def dynamic_type_method_1(self):
    print(f"definitions.DummyDynamicsClass1.dynamic_type_method_1()")

DummyDynamicClass1 = type(
    "DummyDynamicClass1",
    (),
    {
        "__init__": dynamic_type_init_1,
        "method_1": dynamic_type_method_1,
    }
)

# Dynamic Type Creation with types.new_class [Type 3]
import types

def dynamic_type_body_1(ns):
    ns['__init__'] = lambda self, value: setattr(self, 'value', value)
    ns['method_1']  = lambda self: print(f"definitions.DynamicTypeCreation1.method_1()")

DummyDynamicCreationClass1 = types.new_class(
    "DummyDynamicCreationClass1",
    (),
    {},
    dynamic_type_body_1
)

# Metaclass [Type 4]
class DummyMeta1(type):
    def __new__(mcls, name, bases, namespace):
        namespace['method_1'] = lambda self: print("definitions.DummyMeta1.method_1()")
        return super().__new__(mcls, name, bases, namespace)

class WithDummyMeta1(metaclass=DummyMeta1):
    pass

# Abstract Base Class (ABC) [Type 5]
from abc import ABC, abstractmethod

class DummyABC1(ABC):
    @abstractmethod
    def method_1(self):
        pass

class DummyABC1Impl(DummyABC1):
    def method_1(self):
        print("definitions.DummyABC1Impl.method_1()")

# collections.namedtuple [Type 6]
from collections import namedtuple

DummyCollectionsNamedTuple1 = namedtuple("DummyCollectionsNamedTuple1", ["value_1", "value_2"])

# typing.NamedTuple [Type 7]
from typing import NamedTuple

class DummyTypingNamedTuple2(NamedTuple):
    value_1: dict[str, any]
    value_2: list[int]

# @dataclass [Type 8]
from dataclasses import dataclass

@dataclass
class DummyDataclass1:
    value_1: dict[str, any]
    value_2: list[int]

# TypedDict [Type 9]
from typing import TypedDict

class DummyTypedDict1(TypedDict):
    value_1: dict[str, any]
    value_2: list[int]

# NewType [Type 10]
from typing import NewType

DummyNewType1 = NewType("DummyNewType1", dict[str, any])

# TypeVar & Generics [Type 11]
from typing import TypeVar, Generic

T = TypeVar('T')

class DummyGenericClass1(Generic[T]):
    def __init__(self, value: T):
        self.value = value
        
# Protocol [Type 12]
from typing import Protocol

class DummyProtocol1(Protocol):
    def method_1(self):
        pass

class DummyProtocol1Impl(DummyProtocol1):
    def method_1(self):
        print("definitions.DummyProtocol1Impl.method_1()")

# Type Alias [Type 13]
from typing import TypeAlias

DummyTypeAlias1: TypeAlias = dict[str, any]
DummyTypeAlias2 = list[int]
# Only valid for Python 3.12+
type DummyTypeAlias3 = tuple[int, int]

# Enum [Type 14]
from enum import Enum

class DummyEnum1(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
