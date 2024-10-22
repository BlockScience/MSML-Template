## Wiring Diagrams

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("DUMMY Entity")]
EES0(["Total Length"])
EES0 --- EE0
EES1(["Words"])
EES1 --- EE0
end

subgraph X4["DUMMY Length-1 Boundary Wiring"]
direction TB
X1["DUMMY Length-1 ABC Boundary Action"]
X2["DUMMY Letter Count Policy"]
X3["DUMMY Log Results Mechanism"]
X3 --> EES1
X3 --> EES0
X1--"DUMMY ABCDEF Space"--->X2
X2--"DUMMY String Length Space"--->X3
end
```

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("DUMMY Entity")]
EES0(["Total Length"])
EES0 --- EE0
EES1(["Words"])
EES1 --- EE0
end

subgraph X4["DUMMY Length-2 Boundary Wiring"]
direction TB
X1["DUMMY Length-2 ABC Combo Boundary Action"]
X2["DUMMY Letter Count Policy"]
X3["DUMMY Log Results Mechanism"]
X3 --> EES1
X3 --> EES0
X1--"DUMMY ABCDEF Space"--->X2
X2--"DUMMY String Length Space"--->X3
end
```

## Description

The wirings related to only boundary type actions.
## Wirings
1. [[DUMMY Length-1 Boundary Wiring]]
2. [[DUMMY Length-2 Boundary Wiring]]

## Unique Components Used
1. [[DUMMY Length-1 ABC Boundary Action]]
2. [[DUMMY Length-2 ABC Combo Boundary Action]]
3. [[DUMMY Letter Count Policy]]
4. [[DUMMY Log Results Mechanism]]

## Unique Parameters Used
1. [[DUMMY Length Multiplier]]

