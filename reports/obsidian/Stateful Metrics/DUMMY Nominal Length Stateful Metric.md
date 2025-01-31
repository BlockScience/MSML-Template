Description: The number of letters after the multiplier is taken off

Type: [[DUMMY Integer Type]]

Symbol: None

Domain: None

## Parameters Used
1. [[DUMMY Length Multiplier]]

## Variables Used
1. [[DUMMY State]].Total Length

## Python Implementation
```python
def dummy_metric(state, params):
    return state["Dummy"]["Total Length"] // params["DUMMY Length Multiplier"]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/StatefulMetrics/Dummy.py#L1](../../../src/Implementations/Python/StatefulMetrics/Dummy.py#L1)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/StatefulMetrics/Dummy.py#L7](../../../../src/StatefulMetrics/Dummy.py#L7)

