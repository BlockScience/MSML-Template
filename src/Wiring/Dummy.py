dummy_wiring = []

dummy_wiring.append(
    {
        "name": "DUMMY Length-1 Boundary Wiring",
        "components": [
            "DUMMY Length-1 ABC Boundary Action",
            "DUMMY Letter Count Policy",
            "DUMMY State Update Mechanisms",
            "DUMMY Log Simulation Data Mechanism",
        ],
        "description": "Dummy Boundary Block",
        "constraints": [],
        "type": "Stack",
    }
)

dummy_wiring.append(
    {
        "name": "DUMMY Control Wiring",
        "components": [
            "DUMMY Length-1 DEF Control Action",
            "DUMMY Letter Count Policy",
            "DUMMY State Update Mechanisms",
            "DUMMY Log Simulation Data Mechanism",
        ],
        "description": "Dummy Control Block",
        "constraints": [],
        "type": "Stack",
        "optional_indices": [1],
    }
)

dummy_wiring.append(
    {
        "name": "DUMMY Length-2 Boundary Wiring",
        "components": [
            "DUMMY Length-2 ABC Combo Boundary Action",
            "DUMMY Letter Count Policy",
            "DUMMY State Update Mechanisms",
            "DUMMY Log Simulation Data Mechanism",
        ],
        "description": "Dummy Boundary Block",
        "constraints": [],
        "type": "Stack",
    }
)


dummy_wiring.append(
    {
        "name": "DUMMY State Update Mechanisms",
        "components": [
            "DUMMY Update Dummy Entity Mechanism",
            "DUMMY Increment Time Mechanism",
        ],
        "description": "Mechanisms for updating the state of the system",
        "constraints": [],
        "type": "Parallel",
    }
)
