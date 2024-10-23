from .Dummy import (
    dummy_update_dummy_entity_mechanism,
    dummy_increment_time_mechanism,
    dummy_log_simulation_data_mechanism,
)

mechanisms = {
    "DUMMY Update Dummy Entity Mechanism": dummy_update_dummy_entity_mechanism,
    "DUMMY Increment Time Mechanism": dummy_increment_time_mechanism,
    "DUMMY Log Simulation Data Mechanism": dummy_log_simulation_data_mechanism,
}
