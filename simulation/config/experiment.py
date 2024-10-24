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
