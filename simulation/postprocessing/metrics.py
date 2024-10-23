def percent_ending_in_d_metric(metrics, state, params, df):
    metrics["Percent Ending in D"] = (
        df["Word"].apply(lambda x: x[-1] == "D" if len(x) > 0 else None).mean()
    )


def average_d_count_metric(metrics, state, params, df):
    metrics["Average D Count"] = (
        df["Word"].apply(lambda x: x.count("D") if len(x) > 0 else None).mean()
    )
