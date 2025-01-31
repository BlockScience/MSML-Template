## Description

Boundary action which returns a string of length 2 which is some combination of A, B, and C.
## Called By
1. [[DUMMY Entity]]

## Followed By
1. [[DUMMY Letter Count Policy]]

## Constraints

## Codomain Spaces
1. [[DUMMY ABCDEF Space]]

## Metrics Used

## Parameters Used

## Boundary Action Options:
### 1. DUMMY Length-2 ABC Equal Weight Option
#### Description
Equal weighted probability of choosing A, B or C each time
#### Logic
Select A, B, C with equal probabilities
#### Python Implementation
```python
def v1_dummy_boundary2(state, params, spaces):
    first = choice(["A", "B", "C"])
    second = choice(["A", "B", "C"])
    return [{"string": first + second}]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/BoundaryActions/Dummy.py#L8](../../../src/Implementations/Python/BoundaryActions/Dummy.py#L8)

### 2. DUMMY Length-2 ABC Equal Weight 2 Option
#### Description
Equal weighted probability of choosing A, B or C for the first letter, and then equal probability of choose the left over 2 for the next one.
#### Logic
Select A, B, C with equal probabilities. Then choose from the remaining two with equal probability.
#### Python Implementation
```python
def v2_dummy_boundary2(state, params, spaces):
    first = choice(["A", "B", "C"])
    second = choice([x for x in ["A", "B", "C"] if x != first])
    return [{"string": first + second}]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/BoundaryActions/Dummy.py#L14](../../../src/Implementations/Python/BoundaryActions/Dummy.py#L14)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/BoundaryActions/Dummy.py#L33](../../../../src/BoundaryActions/Dummy.py#L33)

