"""
The below code is an example that reads in the above config file, shows how to use it to create a
 `Client` object, and then profiles example tables, writing the results into Tamr.
 Relies on default values and everything being specified by config file.
"""
import tamr_toolbox as tbox


my_config = tbox.utils.config.from_yaml("examples/resources/conf/connect.config.yaml")
my_connect = tbox.data_io.df_connect.client.from_config(my_config)

# profile tables A and B, and write results to Tamr dataset dfconnect_profiling
tbox.data_io.df_connect.client.profile_query_results(
    my_connect,
    dataset_name="dfconnect_profiling",
    queries=["SELECT * FROM TABLE_A", "SELECT * FROM TABLE_B"],
)
