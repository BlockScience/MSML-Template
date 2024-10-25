import matplotlib.pyplot as plt


def plot_length_single_simulation(df):
    df.set_index("Time")["Length (Nominal)"].plot(kind="line")
    plt.ylabel("Length")
    plt.title("Length over Time")
    plt.show()
