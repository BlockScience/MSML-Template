from .types import SimulationLogType, EntityType, DummyABCDEFType, DummyIntegerType
from typing import TypedDict

DUMMYState = TypedDict('DUMMY State', {'Words': DummyABCDEFType, 'Total Length': DummyIntegerType})
GlobalState = TypedDict('Global State', {'Dummy': EntityType, 'Time': DummyIntegerType, 'Simulation Log': SimulationLogType})

state: GlobalState = {"Dummy": None,
"Time": None,
"Simulation Log": None,
}