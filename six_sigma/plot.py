import matplotlib.pyplot as plt
from six_sigma.calc import mean, stddev

LIMIT_COLOR = (0.8, 0.6, 0.0, 0.7)


def create_plot(data: list, upper_limit: float = 0.0, lower_limit: float = 0.0, dataset_name: str = None):
    mean_value = mean(data)
    stddev_value = stddev(data)
    upper_3s = min((mean_value + 3 * stddev_value), 100)
    lower_3s = max((mean_value - 3 * stddev_value), 0)

    if dataset_name:
        plt.title(f"Data of: {dataset_name}")
    plt.xlabel("Number of Value")
    plt.ylabel("Quality [%]")

    plt.axis([0, len(data), 0, 100])
    for index, element in enumerate(data):
        if upper_limit and element > upper_limit:
            plt.plot(index,element, "ro")
        if lower_limit and element < lower_limit:
            plt.plot(index,element, "ro")
        else:
            plt.plot(index,element, "go")

    plt.axhline(y=mean_value, color='b', linestyle='-.')
    plt.axhline(y=upper_3s, color=LIMIT_COLOR, linestyle='--')
    plt.axhline(y=lower_3s, color=LIMIT_COLOR, linestyle='--')
    if upper_limit:
        plt.axhline(y=upper_limit, color='r', linestyle='-')
    if lower_limit:
        plt.axhline(y=lower_limit, color='r', linestyle='-')
    plt.show()


def create_histogramm(data: list, upper_limit: float = 0.0, lower_limit: float = 0.0, dataset_name: str = None):
    mean_value = mean(data)
    stddev_value = stddev(data)
    upper_3s = min((mean_value + 3 * stddev_value), 100)
    lower_3s = max((mean_value - 3 * stddev_value), 0)

    if dataset_name:
        plt.title(f"Histogram of: {dataset_name}")
    plt.xlabel('Quality [%]')
    plt.ylabel('Count')

    count_bins = int((max(data) - min(data)) / 2)

    n, bins, patches = plt.hist(data, count_bins, density=False, facecolor='g')

    plt.axis([min(bins) - 2, max(bins) + 2, 0, max(n) + 2])
    plt.grid(True)

    plt.axvline(x=mean_value, color='b', linestyle='-.')
    plt.axvline(x=upper_3s, color=LIMIT_COLOR, linestyle='--')
    plt.axvline(x=lower_3s, color=LIMIT_COLOR, linestyle='--')
    if upper_limit:
        plt.axvline(x=upper_limit, color='r', linestyle='-')
    if lower_limit:
        plt.axvline(x=lower_limit, color='r', linestyle='-')
    plt.show()
