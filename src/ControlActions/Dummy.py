dummy_control_action_v1_option = {
    "name": "DUMMY Length-1 DEF Equal Weight Option",
    "description": "Equal weighted probability of choosing D, E or F each time",
    "logic": "Select D, E, F with equal probabilities",
}

dummy_control_action_v2_option = {
    "name": "DUMMY Length-1 DEF D Probability Option",
    "description": "Randomly picks between D, E, F based on the 'DUMMY D Probability' Parameter",
    "logic": "Use PARAM['DUMMY D Probability'] for the chance of picking D, (1-['D Probability']) / 2 chance for the other two",
}


dummy_control_action = {
    "name": "DUMMY Length-1 DEF Control Action",
    "description": "Returns any length 1 string equal to D, E or F",
    "constraints": [],
    "control_action_options": [
        dummy_control_action_v1_option,
        dummy_control_action_v2_option,
    ],
    "codomain": [
        "DUMMY ABCDEF Space",
    ],
    "parameters_used": ["DUMMY D Probability"],
}

dummy_control_actions = [dummy_control_action]
