## Description

A mechanism which adds one to the clock time
## Called By
## Domain Spaces
1. [[Empty Space]]
## Constraints
## Metrics Used

## Parameters Used

## Logic
1. Increment the global time by 1

## Updates

1. [[Global]].[[Global State-Time|Time]]
## Python Implementation
```python
def dummy_increment_time_mechanism(state, params, spaces):
    state["Time"] += 1
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Mechanisms/Dummy.py#L8](../../../src/Implementations/Python/Mechanisms/Dummy.py#L8)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Mechanisms/Dummy.py#L18](../../../../src/Mechanisms/Dummy.py#L18)

