def compute_starting_total_length(state, params):
    state["Dummy"]["Total Length"] = params["DUMMY Length Multiplier"] * len(
        state["Dummy"]["Words"]
    )
    return state
