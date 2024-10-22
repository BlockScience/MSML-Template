dummy_boundary_action_v1_option = {
    "name": "V1 Dummy Boundary Action Option",
    "description": "Equal weighted probability of choosing A, B or C",
    "logic": "Select A, B, C with equal probabilities",
}

dummy_boundary_action = {
    "name": "DUMMY Length-1 ABC Boundary Action",
    "description": "Randomly returns either A, B, C",
    "constraints": [],
    "boundary_action_options": [dummy_boundary_action_v1_option],
    "called_by": ["DUMMY Entity"],
    "codomain": [
        "DUMMY ABC Space",
    ],
    "parameters_used": [],
}


dummy_boundary_action2_v1_option = {
    "name": "V1 Dummy Boundary Action 2 Option",
    "description": "Equal weighted probability of choosing A, B or C each time",
    "logic": "Select A, B, C with equal probabilities",
}

dummy_boundary_action2_v2_option = {
    "name": "V2 Dummy Boundary Action 2 Option",
    "description": "Equal weighted probability of choosing A, B or C for the first letter, and then equal probability of choose the left over 2 for the next one.",
    "logic": "Select A, B, C with equal probabilities. Then choose from the remaining two with equal probability.",
}

dummy_boundary_action2 = {
    "name": "DUMMY Length-2 ABC Combo Boundary Action",
    "description": "Boundary action which returns a string of length 2 which is some combination of A, B, and C.",
    "constraints": [],
    "boundary_action_options": [
        dummy_boundary_action2_v1_option,
        dummy_boundary_action2_v2_option,
    ],
    "called_by": ["DUMMY Entity"],
    "codomain": [
        "DUMMY ABC Space",
    ],
    "parameters_used": [],
}

dummy_boundary_actions = [dummy_boundary_action, dummy_boundary_action2]
