## Description

Boundary action which returns a string of length 2 which is some combination of A, B, and C.
## Called By
1. [[DUMMY Entity]]

## Followed By
1. [[DUMMY Letter Count Policy]]

## Constraints

## Codomain Spaces
1. [[DUMMY ABCDEF Space]]

## Boundary Action Options:
### 1. DUMMY Length-2 ABC Equal Weight Option
#### Description
Equal weighted probability of choosing A, B or C each time
#### Logic
Select A, B, C with equal probabilities

### 2. DUMMY Length-2 ABC Equal Weight 2 Option
#### Description
Equal weighted probability of choosing A, B or C for the first letter, and then equal probability of choose the left over 2 for the next one.
#### Logic
Select A, B, C with equal probabilities. Then choose from the remaining two with equal probability.

