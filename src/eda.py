import matplotlib.pyplot as plt

def plot_basic_trends(df):
    plt.figure()
    plt.plot(df['date'], df['temperature'])
    plt.title("Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.savefig("outputs/plots/temp_trend.png")
    plt.close()