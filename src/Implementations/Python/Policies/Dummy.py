def dummy_letter_count_policy(state, params, spaces):
    starting_string = spaces[0]["string"]
    unique = len(set(list(starting_string)))
    length = state["Metrics"]["DUMMY Multiplied Length Metric"](state, params, spaces)
    return [{"string": starting_string, "unique_length": unique, "length": length}]
