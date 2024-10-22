dummy_wiring = []

dummy_wiring.append(
    {
        "name": "DUMMY Length-1 Boundary Wiring",
        "components": [
            "DUMMY Length-1 ABC Boundary Action",
            "DUMMY Letter Count Policy",
            "DUMMY Log Results Mechanism",
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
            "DUMMY Log Results Mechanism",
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
            "DUMMY Log Results Mechanism",
        ],
        "description": "Dummy Boundary Block",
        "constraints": [],
        "type": "Stack",
    }
)
