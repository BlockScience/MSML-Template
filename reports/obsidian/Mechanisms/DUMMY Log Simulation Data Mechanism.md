## Description

A mechanism for logging simulation data
## Called By
## Domain Spaces
1. [[Empty Space]]
## Constraints
## Metrics Used

## Parameters Used

## Logic
Append simulation data to the simulation log

## Updates

1. [[Global]].[[Global State-Simulation Log|Simulation Log]]
## Python Implementation
```python
def dummy_log_simulation_data_mechanism(state, params, spaces):
    state["Simulation Log"].append(
        {
            "Time": state["Time"],
            "Word": state["Dummy"]["Words"],
            "Length (Multiplied)": state["Dummy"]["Total Length"],
        }
    )
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Mechanisms/Dummy.py#L12](../../../src/Implementations/Python/Mechanisms/Dummy.py#L12)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Mechanisms/Dummy.py#L30](../../../../src/Mechanisms/Dummy.py#L30)

