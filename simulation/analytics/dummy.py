import matplotlib.pyplot as plt


def plot_length_single_simulation(df):
    df.set_index("Time")["Length (Nominal)"].plot(kind="line")
    plt.ylabel("Length")
    plt.title("Length over Time")
    plt.show()


def plot_length_experiment_simulation(df):
    df.groupby(["Time", "Experiment"])["Length (Nominal)"].mean().unstack().plot(
        kind="line"
    )
    plt.ylabel("Average Length")
    plt.title("Average Length by Experiment over Time")
    plt.legend()
    plt.show()


def plot_d_count_experiment_simulation(df):
    df.groupby(["Time", "Experiment"])["D Count"].mean().unstack().plot(kind="line")
    plt.ylabel("Average D Count")
    plt.title("Average D Count by Experiment over Time")
    plt.legend()
    plt.show()
