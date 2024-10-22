from typing import NewType, TypedDict

DummyType1 = {"name": "Dummy Type 1", "type": "DummyType1", "notes": ""}

DummyType2 = {"name": "Dummy Type 2", "type": "DummyType2", "notes": ""}


DummyCompoundType = {
    "name": "Dummy Compound Type",
    "type": "DummyCompoundType",
    "notes": "",
}

EntityType = {
    "name": "Entity Type",
    "type": "EntityType",
    "notes": "",
}

DummyABCType = {
    "name": "DUMMY ABC Type",
    "type": "DummyABCType",
    "notes": "This type will be a string but is constrained to only taking on the values of A, B and C",
}


dummy_types = [DummyType1, DummyType2, DummyCompoundType, EntityType, DummyABCType]
