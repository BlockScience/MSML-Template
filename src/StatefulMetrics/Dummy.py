dummy_stateful_metric = {
    "name": "DUMMY Stateful Metrics",
    "notes": "A set of dummy stateful metrics",
    "metrics": [
        {
            "type": "DUMMY Integer Type",
            "name": "DUMMY Nominal Length Stateful Metric",
            "description": "The number of letters after the multiplier is taken off",
            "variables_used": [("DUMMY State", "Total Length")],
            "parameters_used": ["DUMMY Length Multiplier"],
            "symbol": None,
            "domain": None,
        }
    ],
}

dummy_stateful_metrics = [dummy_stateful_metric]
