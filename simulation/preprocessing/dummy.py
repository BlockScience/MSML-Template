def compute_starting_total_length(state, params):
    state["Dummy"]["Total Length"] = params["DUMMY Length Multiplier"] * len(
        state["Dummy"]["Words"]
    )
    return state


def check_d_probability(params):
    # If the functional parameterization is set to equal weight, override the D probability parameter to always be 1/3
    if (
        params["FP DUMMY Length-1 DEF Control Action"]
        == "DUMMY Length-1 DEF Equal Weight Option"
    ):
        params["DUMMY D Probability"] = 1 / 3
    return params
