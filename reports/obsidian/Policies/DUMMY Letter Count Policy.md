## Description

The policy returns the original variable for the passed string as well as all unique letters used and the total number of characters in the string times the multiplier parameter.
## Called By
1. [[DUMMY Length-1 ABC Boundary Action]]
2. [[DUMMY Length-1 DEF Control Action]]
3. [[DUMMY Length-2 ABC Combo Boundary Action]]
## Domain Spaces
1. [[DUMMY ABCDEF Space]]
## Followed By
1. [[DUMMY Update Dummy Entity Mechanism]]
2. [[DUMMY Update Dummy Entity Mechanism]]
## Codomain Spaces
1. [[DUMMY String Length Space]]
## Constraints
1. The string in the first domain space must only contain the letters of A, B, C, D, E, F
## Parameters Used
1. [[DUMMY Length Multiplier]]
## Metrics Used
1. [[DUMMY Multiplied Length Metric]]
## Policy Options
### 1. DUMMY Letter Count Policy V1
#### Description
Returns the original variable for the passed string as well as all unique letters used and the total number of characters in the string
#### Logic
Implementation is to get the set of the list of characters and then the length of the domain string times the multiplier.
#### Python Implementation
```python
def dummy_letter_count_policy(state, params, spaces):
    starting_string = spaces[0]["string"]
    unique = len(set(list(starting_string)))
    length = state["Metrics"]["DUMMY Multiplied Length Metric"](state, params, spaces)
    return [{"string": starting_string, "unique_length": unique, "length": length}]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Policies/Dummy.py#L1](../../../src/Implementations/Python/Policies/Dummy.py#L1)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Policies/Dummy.py#L2](../../../../src/Policies/Dummy.py#L2)

