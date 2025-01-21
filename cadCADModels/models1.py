import os
import sys
from copy import deepcopy

sys.path.append(os.path.abspath("../.."))
from MSML.src.math_spec_mapping import load_from_json


from src import math_spec_json
from simulation import compute_starting_total_length, check_d_probability

ms = load_from_json(deepcopy(math_spec_json))

blocks1 = [
    "DUMMY Length-2 Boundary Wiring",
    "DUMMY Length-1 Boundary Wiring",
    "DUMMY Control Wiring",
]

model1 = ms.build_cadCAD(
    blocks1,
    state_preperation_functions=[compute_starting_total_length],
    parameter_preperation_functions=[check_d_probability],
)

blocks2 = [
    "DUMMY Length-2 Boundary Wiring",
    "DUMMY Length-1 Boundary Wiring",
]

model2 = ms.build_cadCAD(
    blocks2,
    state_preperation_functions=[compute_starting_total_length],
    parameter_preperation_functions=[check_d_probability],
)
