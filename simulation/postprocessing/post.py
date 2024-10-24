import pandas as pd


def post_processing_function(state, params):
    df = pd.DataFrame(state["Simulation Log"])
    df["Length (Nominal)"] = (
        df["Length (Multiplied)"] / params["DUMMY Length Multiplier"]
    )
    df["D Count"] = df["Word"].apply(lambda x: x.count("D") if len(x) > 0 else None)
    return df
