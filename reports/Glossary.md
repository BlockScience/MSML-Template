# Glossary

## Entities

**DUMMY Entity**: A local state within the model


## State

### Global State

### Notes

### Variable Table
| Name | Description | Type | Symbol | Domain |
| --- | --- | --- | --- | --- |
|Dummy|The dummy entity|Entity Type|||
|Time|The clock time|DUMMY Integer Type|||
|Simulation Log|The simulation log holding historical data|Simulation Log Type|||


### DUMMY State

### Notes
The state of the local DUMMY entity
### Variable Table
| Name | Description | Type | Symbol | Domain |
| --- | --- | --- | --- | --- |
|Words|All words that were created|DUMMY ABCDEF Type|||
|Total Length|The total length of words * multiplier|DUMMY Integer Type|||




## Types

**DUMMY ABCDEF Type**: This type will be a string but is constrained to only taking on the values of [A, B, C, D, E, F]

**DUMMY Integer Type**: A simple integer type

**DUMMY Decimal Type**: A decimal value

**Entity Type**: 

**Simulation Log Type**: Will be a list of entries expanding over time



## Spaces

**Terminating Space**: Built-in space for denoting termination of block

**Empty Space**: Built-in space for denoting returning no data

**DUMMY ABCDEF Space**: None

**DUMMY String Length Space**: None



## Boundary Actions

**DUMMY Length-1 ABC Boundary Action**: Randomly returns either A, B, C

**DUMMY Length-2 ABC Combo Boundary Action**: Boundary action which returns a string of length 2 which is some combination of A, B, and C.



## Control Actions

**DUMMY Length-1 DEF Control Action**: Returns any length 1 string equal to D, E or F



## Policies

**DUMMY Letter Count Policy**: The policy returns the original variable for the passed string as well as all unique letters used and the total number of characters in the string times the multiplier parameter.



## Mechanisms

**DUMMY Update Dummy Entity Mechanism**: A mechanism which appends the word just added and also increments the total length

**DUMMY Increment Time Mechanism**: A mechanism which adds one to the clock time

**DUMMY Log Simulation Data Mechanism**: A mechanism for logging simulation data



## Wiring

**DUMMY State Update Mechanisms**: Mechanisms for updating the state of the system

**DUMMY Length-1 Boundary Wiring**: Dummy Boundary Block

**DUMMY Control Wiring**: Dummy Control Block

**DUMMY Length-2 Boundary Wiring**: Dummy Boundary Block



## Parameters

**DUMMY D Probability**: The probability that D is chosen

**DUMMY Length Multiplier**: A multiplier to multiply into length calculations



## Stateful Metrics

**DUMMY Stateful Metrics**: A set of dummy stateful metrics



## Metrics

**DUMMY Multiplied Length Metric**: A simple metric which, given a [[DUMMY ABCDEF Space]] and the [[DUMMY Length Multiplier]] returns an integer of multiplied length.



