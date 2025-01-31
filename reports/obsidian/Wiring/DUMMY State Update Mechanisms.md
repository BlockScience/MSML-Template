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
EES2(["Time"])
EES2 --- EE1
end

subgraph X5["DUMMY State Update Mechanisms"]
direction TB
X1["DUMMY Update Dummy Entity Mechanism"]
X1 --"State Update"--> EES0
X1 --"State Update"--> EES1
X2["DUMMY Increment Time Mechanism"]
X2 --"State Update"--> EES2
X3[Domain]

direction LR
direction TB
X3 --"<a href='DUMMY String Length Space' class=internal-link>DUMMY String Length Space</a>"--> X1
X3 --> X2
end
class X1 internal-link;
class X2 internal-link;
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
EES2(["Time"])
EES2 --- EE1
end

subgraph X5["DUMMY State Update Mechanisms"]
direction TB
X1["DUMMY Update Dummy Entity Mechanism"]
X1 --"State Update"--> EES0
X1 --"State Update"--> EES1
X2["DUMMY Increment Time Mechanism"]
X2 --"State Update"--> EES2
X3[Domain]

direction LR
direction TB
X3 --"<a href='DUMMY String Length Space' class=internal-link>DUMMY String Length Space</a>"--> X1
X3 --> X2
end
class X1 internal-link;
class X2 internal-link;
class X4 internal-link;
class EE0 internal-link;
class EE1 internal-link;

```

## Description

Block Type: Parallel Block
Mechanisms for updating the state of the system
## Components
1. [[DUMMY Update Dummy Entity Mechanism]]
2. [[DUMMY Increment Time Mechanism]]

## All Blocks
1. [[DUMMY Increment Time Mechanism]]
2. [[DUMMY Update Dummy Entity Mechanism]]

## Constraints

## Domain Spaces
1. [[DUMMY String Length Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[DUMMY String Length Space]]
2. [[Empty Space]]
3. [[Terminating Space]]

## Metrics Used

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[DUMMY Entity]].[[DUMMY State-Total Length|Total Length]]
2. [[DUMMY Entity]].[[DUMMY State-Words|Words]]
3. [[Global]].[[Global State-Time|Time]]

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Wiring/Dummy.py#L9](../../../../src/Wiring/Dummy.py#L9)

