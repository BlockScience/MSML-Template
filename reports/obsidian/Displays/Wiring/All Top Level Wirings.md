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

subgraph X9["DUMMY Control Wiring"]
direction TB
X1["DUMMY Length-1 DEF Control Action"]
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
X2-."<a href='DUMMY String Length Space' class=internal-link>DUMMY String Length Space</a>"..->X7
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

The wirings which are not components of other wirings.
## Wirings
1. [[DUMMY Length-1 Boundary Wiring]]
2. [[DUMMY Length-2 Boundary Wiring]]
3. [[DUMMY Control Wiring]]

## Unique Components Used
1. [[DUMMY Increment Time Mechanism]]
2. [[DUMMY Length-1 ABC Boundary Action]]
3. [[DUMMY Length-1 DEF Control Action]]
4. [[DUMMY Length-2 ABC Combo Boundary Action]]
5. [[DUMMY Letter Count Policy]]
6. [[DUMMY Log Simulation Data Mechanism]]
7. [[DUMMY Update Dummy Entity Mechanism]]

## Unique Parameters Used
1. [[DUMMY D Probability]]
2. [[DUMMY Length Multiplier]]

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../../src/Displays/wiring.py#L4](../../../../../src/Displays/wiring.py#L4)

