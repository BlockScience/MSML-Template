dummy_parameter_set = {
    "name": "DUMMY Parameter Set",
    "notes": "A set of dummy parameters",
    "parameters": [
        {
            "variable_type": "DUMMY Decimal Type",
            "name": "DUMMY D Probability",
            "description": "The probability that D is chosen",
            "symbol": None,
            "domain": "[0, 1]",
            "parameter_class": "Behavioral",
        },
        {
            "variable_type": "DUMMY Integer Type",
            "name": "DUMMY Length Multiplier",
            "description": "A multiplier to multiply into length calculations",
            "symbol": None,
            "domain": r"$\mathbb{Z}$",
            "parameter_class": "System",
        },
    ],
}


dummy_parameter_sets = [dummy_parameter_set]
