## Wiring Diagrams

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("DUMMY Entity")]
EE1[("Global")]
EES0(["Total Length"])
EES0 --- EE0
EES1(["Words"])
EES1 --- EE0
EES2(["Simulation Log"])
EES2 --- EE1
EES3(["Time"])
EES3 --- EE1
end

subgraph X9["DUMMY Length-1 Boundary Wiring"]
direction TB
X1["DUMMY Length-1 ABC Boundary Action"]
X2["DUMMY Letter Count Policy"]
subgraph X7["DUMMY State Update Mechanisms"]
direction TB
X3["DUMMY Update Dummy Entity Mechanism"]
X3 --> EES1
X3 --> EES0
X4["DUMMY Increment Time Mechanism"]
X4 --> EES3
X5[Domain]

direction LR
direction TB
X5 --"DUMMY String Length Space"--> X3
X5 --> X4
end
X8["DUMMY Log Simulation Data Mechanism"]
X8 --> EES2
X1--"DUMMY ABCDEF Space"--->X2
X2--"DUMMY String Length Space"--->X7
X7--->X8
end
```

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("DUMMY Entity")]
EE1[("Global")]
EES0(["Total Length"])
EES0 --- EE0
EES1(["Words"])
EES1 --- EE0
EES2(["Simulation Log"])
EES2 --- EE1
EES3(["Time"])
EES3 --- EE1
end

subgraph X9["DUMMY Length-2 Boundary Wiring"]
direction TB
X1["DUMMY Length-2 ABC Combo Boundary Action"]
X2["DUMMY Letter Count Policy"]
subgraph X7["DUMMY State Update Mechanisms"]
direction TB
X3["DUMMY Update Dummy Entity Mechanism"]
X3 --> EES1
X3 --> EES0
X4["DUMMY Increment Time Mechanism"]
X4 --> EES3
X5[Domain]

direction LR
direction TB
X5 --"DUMMY String Length Space"--> X3
X5 --> X4
end
X8["DUMMY Log Simulation Data Mechanism"]
X8 --> EES2
X1--"DUMMY ABCDEF Space"--->X2
X2--"DUMMY String Length Space"--->X7
X7--->X8
end
```

## Description

The wirings related to only boundary type actions.
## Wirings
1. [[DUMMY Length-1 Boundary Wiring]]
2. [[DUMMY Length-2 Boundary Wiring]]

## Unique Components Used
1. [[DUMMY Increment Time Mechanism]]
2. [[DUMMY Length-1 ABC Boundary Action]]
3. [[DUMMY Length-2 ABC Combo Boundary Action]]
4. [[DUMMY Letter Count Policy]]
5. [[DUMMY Log Simulation Data Mechanism]]
6. [[DUMMY Update Dummy Entity Mechanism]]

## Unique Parameters Used
1. [[DUMMY Length Multiplier]]

