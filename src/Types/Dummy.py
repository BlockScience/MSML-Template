from typing import NewType, TypedDict


EntityType = {
    "name": "Entity Type",
    "type": "EntityType",
    "notes": "",
}

DummyABCDEFType = {
    "name": "DUMMY ABCDEF Type",
    "type": "DummyABCDEFType",
    "notes": "This type will be a string but is constrained to only taking on the values of [A, B, C, D, E, F]",
}

DummyIntegerType = {
    "name": "DUMMY Integer Type",
    "type": "DummyIntegerType",
    "notes": "A simple integer type",
}

DummyDecimalType = {
    "name": "DUMMY Decimal Type",
    "type": "DummyDecimalType",
    "notes": "A decimal value",
}


dummy_types = [
    EntityType,
    DummyABCDEFType,
    DummyIntegerType,
    DummyDecimalType,
]
