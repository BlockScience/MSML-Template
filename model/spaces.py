from .types import DummyIntegerType, DummyABCDEFType
from typing import TypedDict

TerminatingSpace = TypedDict('Terminating Space', {})
EmptySpace = TypedDict('Empty Space', {})
DUMMYABCDEFSpace = TypedDict('DUMMY ABCDEF Space', {'string': DummyABCDEFType})
DUMMYStringLengthSpace = TypedDict('DUMMY String Length Space', {'string': DummyABCDEFType, 'length': DummyIntegerType, 'unique_length': DummyIntegerType})
