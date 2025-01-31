## Wiring Diagram (Zoomed Out)

- For display of only depth of 1 in the components/nested wirings
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

subgraph X5["DUMMY Length-1 Boundary Wiring"]
direction TB
X1["DUMMY Length-1 ABC Boundary Action"]
X2["DUMMY Letter Count Policy"]
X3["DUMMY State Update Mechanisms"]
X3 --"State Update"--> EES0
X3 --"State Update"--> EES1
X3 --"State Update"--> EES3
X4["DUMMY Log Simulation Data Mechanism"]
X4 --"State Update"--> EES2
X1--"<a href='DUMMY ABCDEF Space' class=internal-link>DUMMY ABCDEF Space</a>"--->X2
X2--"<a href='DUMMY String Length Space' class=internal-link>DUMMY String Length Space</a>"--->X3
X3--->X4
end
class X1 internal-link;
class X2 internal-link;
class X3 internal-link;
class X4 internal-link;
class EE0 internal-link;
class EE1 internal-link;

```

## Wiring Diagram

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
X3 --"State Update"--> EES0
X3 --"State Update"--> EES1
X4["DUMMY Increment Time Mechanism"]
X4 --"State Update"--> EES3
X5[Domain]

direction LR
direction TB
X5 --"<a href='DUMMY String Length Space' class=internal-link>DUMMY String Length Space</a>"--> X3
X5 --> X4
end
X8["DUMMY Log Simulation Data Mechanism"]
X8 --"State Update"--> EES2
X1--"<a href='DUMMY ABCDEF Space' class=internal-link>DUMMY ABCDEF Space</a>"--->X2
X2--"<a href='DUMMY String Length Space' class=internal-link>DUMMY String Length Space</a>"--->X7
X7--->X8
end
class X1 internal-link;
class X2 internal-link;
class X3 internal-link;
class X4 internal-link;
class X6 internal-link;
class X8 internal-link;
class EE0 internal-link;
class EE1 internal-link;

```

## Description

Block Type: Stack Block
Dummy Boundary Block
## Components
1. [[DUMMY Length-1 ABC Boundary Action]]
2. [[DUMMY Letter Count Policy]]
3. [[DUMMY State Update Mechanisms]]
4. [[DUMMY Log Simulation Data Mechanism]]

## All Blocks
1. [[DUMMY Increment Time Mechanism]]
2. [[DUMMY Length-1 ABC Boundary Action]]
3. [[DUMMY Letter Count Policy]]
4. [[DUMMY Log Simulation Data Mechanism]]
5. [[DUMMY Update Dummy Entity Mechanism]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Terminating Space]]

## All Spaces Used
1. [[DUMMY ABCDEF Space]]
2. [[DUMMY String Length Space]]
3. [[Empty Space]]
4. [[Terminating Space]]

## Metrics Used
1. [[DUMMY Multiplied Length Metric]]

## Parameters Used
1. [[DUMMY Length Multiplier]]

## Called By

## Calls

## All State Updates
1. [[DUMMY Entity]].[[DUMMY State-Total Length|Total Length]]
2. [[DUMMY Entity]].[[DUMMY State-Words|Words]]
3. [[Global]].[[Global State-Simulation Log|Simulation Log]]
4. [[Global]].[[Global State-Time|Time]]

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Wiring/Dummy.py#L5](../../../../src/Wiring/Dummy.py#L5)

