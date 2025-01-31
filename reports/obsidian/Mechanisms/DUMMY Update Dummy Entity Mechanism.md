## Description

A mechanism which appends the word just added and also increments the total length
## Called By
1. [[DUMMY Letter Count Policy]]
2. [[DUMMY Letter Count Policy]]
## Domain Spaces
1. [[DUMMY String Length Space]]
## Constraints
## Metrics Used

## Parameters Used

## Logic
1. Append the string from DOMAIN[0] to the Words state variable for DUMMY entity
    2. Increment the Total Length state variable by the length from DOMAIN[0]

## Updates

1. [[DUMMY Entity]].[[DUMMY State-Words|Words]]
2. [[DUMMY Entity]].[[DUMMY State-Total Length|Total Length]]
## Python Implementation
```python
def dummy_update_dummy_entity_mechanism(state, params, spaces):
    new_string = spaces[0]["string"]
    new_length = spaces[0]["length"]
    state["Dummy"]["Words"] += new_string
    state["Dummy"]["Total Length"] += new_length
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Mechanisms/Dummy.py#L1](../../../src/Implementations/Python/Mechanisms/Dummy.py#L1)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Mechanisms/Dummy.py#L2](../../../../src/Mechanisms/Dummy.py#L2)

