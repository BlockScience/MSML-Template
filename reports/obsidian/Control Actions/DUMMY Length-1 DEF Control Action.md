## Description

Returns any length 1 string equal to D, E or F
## Followed By
1. [[DUMMY Letter Count Policy]]

## Constraints
## Codomain Spaces
1. [[DUMMY ABCDEF Space]]

## Control Action Options:
### 1. DUMMY Length-1 DEF Equal Weight Option
#### Description
Equal weighted probability of choosing D, E or F each time
#### Logic
Select D, E, F with equal probabilities

### 2. DUMMY Length-1 DEF D Probability Option
#### Description
Randomly picks between D, E, F based on the 'DUMMY D Probability' Parameter
#### Logic
Use PARAM['DUMMY D Probability'] for the chance of picking D, (1-['D Probability']) / 2 chance for the other two

