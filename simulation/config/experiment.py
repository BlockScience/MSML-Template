blocks = ["DUMMY Log Simulation Data Mechanism"]
blocks.extend(["DUMMY Length-2 Boundary Wiring", "DUMMY Length-1 Boundary Wiring"] * 10)
blocks.extend(
    [
        "DUMMY Length-2 Boundary Wiring",
        "DUMMY Length-1 Boundary Wiring",
        "DUMMY Control Wiring",
    ]
    * 10
)

experiments_map = {}


experiments_map["Baseline"] = {
    "Name": "Baseline",
    "Param Modifications": None,
    "State Modifications": None,
    "Blocks": blocks,
    "Monte Carlo Runs": 5,
}

experiments_map["Control Option V2 Low D Probability"] = {
    "Name": "Control Option V2 Low D Probability",
    "Param Modifications": {
        "FP DUMMY Length-1 DEF Control Action": "DUMMY Length-1 DEF D Probability Option",
        "DUMMY D Probability": 0.1,
    },
    "State Modifications": None,
    "Blocks": blocks,
    "Monte Carlo Runs": 5,
}

experiments_map["Control Option V2 High D Probability"] = {
    "Name": "Control Option V2 High D Probability",
    "Param Modifications": {
        "FP DUMMY Length-1 DEF Control Action": "DUMMY Length-1 DEF D Probability Option",
        "DUMMY D Probability": 0.9,
    },
    "State Modifications": None,
    "Blocks": blocks,
    "Monte Carlo Runs": 5,
}
