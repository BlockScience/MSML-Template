def dummy_update_dummy_entity_mechanism(state, params, spaces):
    new_string = spaces[0]["string"]
    new_length = spaces[0]["length"]
    state["Dummy"]["Words"] += new_string
    state["Dummy"]["Total Length"] += new_length


def dummy_increment_time_mechanism(state, params, spaces):
    state["Time"] += 1
