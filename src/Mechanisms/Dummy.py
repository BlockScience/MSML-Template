dummy_mechanism = {
    "name": "DUMMY Log Results Mechanism",
    "description": "A mechanism which appends the word just added and also increments the total length",
    "constraints": [],
    "logic": """1. Append the string from DOMAIN[0] to the Words state variable for DUMMY entity
    2. Increment the Total Length state variable by the length from DOMAIN[0]""",
    "domain": [
        "DUMMY String Length Space",
    ],
    "parameters_used": [],
    "updates": [("DUMMY", "Words", False), ("DUMMY", "Total Length", False)],
}

dummy_mechanisms = [dummy_mechanism]
