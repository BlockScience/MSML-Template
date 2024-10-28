from copy import deepcopy

params_base = {
    "DUMMY D Probability": 0.5,
    "DUMMY Length Multiplier": 3,
    "FP DUMMY Length-1 DEF Control Action": "DUMMY Length-1 DEF Equal Weight Option",
    "FP DUMMY Length-2 ABC Combo Boundary Action": "DUMMY Length-2 ABC Equal Weight Option",
}

params_test1 = deepcopy(params_base)
params_test1["DUMMY D Probability"] = 1
params_test1["FP DUMMY Length-1 DEF Control Action"] = (
    "DUMMY Length-1 DEF D Probability Option"
)


params_test2 = deepcopy(params_base)
params_test2["DUMMY D Probability"] = 0
params_test2["FP DUMMY Length-1 DEF Control Action"] = (
    "DUMMY Length-1 DEF D Probability Option"
)
