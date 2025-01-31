## Description

Returns any length 1 string equal to D, E or F
## Followed By
1. [[DUMMY Letter Count Policy]]

## Constraints
## Codomain Spaces
1. [[DUMMY ABCDEF Space]]

## Metrics Used

## Parameters Used
1. [[DUMMY D Probability]]

## Control Action Options:
### 1. DUMMY Length-1 DEF Equal Weight Option
#### Description
Equal weighted probability of choosing D, E or F each time
#### Logic
Select D, E, F with equal probabilities
#### Python Implementation
```python
def v1_dummy_control(state, params, spaces):
    return [{"string": choice(["D", "E", "F"])}]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/ControlActions/Dummy.py#L4](../../../src/Implementations/Python/ControlActions/Dummy.py#L4)

### 2. DUMMY Length-1 DEF D Probability Option
#### Description
Randomly picks between D, E, F based on the 'DUMMY D Probability' Parameter
#### Logic
Use PARAM['DUMMY D Probability'] for the chance of picking D, (1-['D Probability']) / 2 chance for the other two
#### Python Implementation
```python
def v2_dummy_control(state, params, spaces):
    p1 = params["DUMMY D Probability"]
    p2 = (1 - p1) / 2
    return [{"string": choices(["D", "E", "F"], weights=[p1, p2, p2])[0]}]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/ControlActions/Dummy.py#L8](../../../src/Implementations/Python/ControlActions/Dummy.py#L8)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/ControlActions/Dummy.py#L15](../../../../src/ControlActions/Dummy.py#L15)

