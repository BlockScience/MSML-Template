Description: A simple metric which, given a [[DUMMY ABCDEF Space]] and the [[DUMMY Length Multiplier]] returns an integer of multiplied length.

Type: [[DUMMY Integer Type]]

Symbol: None

## Logic
Multiply the length of the string in the domain space by [[DUMMY Length Multiplier]]

## Parameters Used
1. [[DUMMY Length Multiplier]]

## Variables Used

## Domain Spaces
1. [[DUMMY ABCDEF Space]]
## Metrics Used
## Python Implementation
```python
def dummy_multiplied_length_metric(state, params, spaces):
    return len(spaces[0]["string"]) * params["DUMMY Length Multiplier"]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Metrics/Dummy.py#L1](../../../src/Implementations/Python/Metrics/Dummy.py#L1)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Metrics/Dummy.py#L7](../../../../src/Metrics/Dummy.py#L7)

