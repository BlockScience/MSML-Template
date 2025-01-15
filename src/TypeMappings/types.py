from typing import TypedDict, List

mapping = {
    "DummyABCDEFType": str,
    "DummyIntegerType": int,
    "DummyDecimalType": float,
    "EntityType": TypedDict("EntityType", {"Words": str, "Total Length": int}),
    "SimulationLogType": List[
        TypedDict(
            "SimulationLogEntry", {"Time": int, "Word": str, "Length (Multiplied)": int}
        )
    ],
}
