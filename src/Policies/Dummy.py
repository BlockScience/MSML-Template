dummy_policy_option1 = {
    "name": "DUMMY Letter Count Policy V1",
    "description": "Returns the original variable for the passed string as well as all unique letters used and the total number of characters in the string",
    "logic": """Implementation is to get the set of the list of characters and then the length of the domain string times the multiplier.""",
}

dummy_policy = {
    "name": "DUMMY Letter Count Policy",
    "description": "The policy returns the original variable for the passed string as well as all unique letters used and the total number of characters in the string times the multiplier parameter.",
    "constraints": [
        "The string in the first domain space must only contain the letters of A, B, C, D, E, F"
    ],
    "policy_options": [dummy_policy_option1],
    "domain": [
        "DUMMY ABCDEF Space",
    ],
    "codomain": [
        "DUMMY String Length Space",
    ],
    "parameters_used": ["DUMMY Length Multiplier"],
    "metrics_used": [],
}

dummy_policies = [dummy_policy]
