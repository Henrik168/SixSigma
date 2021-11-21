import matplotlib.pyplot as plt
from six_sigma.calc import mean, stddev
from typing import Tuple


class Plot:
    LIMIT_COLOR = (0.8, 0.6, 0.0, 0.7)

    def __init__(self,
                 y_label: str = None,
                 x_data_label: str = None,
                 x_hist_label: str = None,
                 y_min: float = None,
                 y_max: float = None):
        self.figure_index: int = 0
        self.figures = dict()
        self.y_label = y_label
        self.x_data_label = x_data_label
        self.x_hist_label = x_hist_label
        self.y_min = y_min
        self.y_max = y_max

    @staticmethod
    def calc_sigma(data: list) -> Tuple:
        mean_value = mean(data)
        stddev_value = stddev(data)
        upper_3s = min((mean_value + 3 * stddev_value), 100)
        lower_3s = max((mean_value - 3 * stddev_value), 0)
        return mean_value, stddev_value, lower_3s, upper_3s

    @staticmethod
    def in_bounds(lower, value, upper) -> bool:
        return lower <= value <= upper

    @staticmethod
    def plot_hist(data, ax_hist):
        # no labels
        ax_hist.tick_params(axis="y", labelleft=False)

        # now determine nice limits by hand:
        binwidth = 2
        xmax = max(data)
        lim = (int(xmax / binwidth) + 1) * binwidth

        bins = [bin1 for bin1 in range(-lim, lim + binwidth, binwidth)]
        ax_hist.hist(data, bins=bins, orientation='horizontal')

    def plot_scatter(self, data, ax, lower_limit, upper_limit):
        mean_value, stddev_value, lower_3s, upper_3s = self.calc_sigma(data)
        y_min = self.y_min if self.y_min is not None else min(data)
        y_max = self.y_max if self.y_max is not None else max(data)
        # the scatter plot:
        ax.axis([0, len(data), y_min, y_max])

        for index, value in enumerate(data):
            if not self.in_bounds(lower_limit, value, upper_limit):
                ax.plot(index, value, "ro")
            else:
                ax.plot(index, value, "go")

        ax.axhline(y=mean_value, color='b', linestyle='-.')
        ax.axhline(y=upper_3s, color=self.LIMIT_COLOR, linestyle='--')
        ax.axhline(y=lower_3s, color=self.LIMIT_COLOR, linestyle='--')
        ax.axhline(y=upper_limit, color='r', linestyle='-')
        ax.axhline(y=lower_limit, color='r', linestyle='-')

    def add_plot(self, data: list, title: str, upper_limit: float, lower_limit: float) -> None:

        fig = plt.figure(num=self.figure_index, figsize=[10, 7])
        gs = fig.add_gridspec(1, 2, width_ratios=(7, 3),
                              left=0.1, right=0.9, bottom=0.2, top=0.9,
                              wspace=0.1, hspace=0.05)

        ax = fig.add_subplot(gs[0, 0])
        ax_hist = fig.add_subplot(gs[0, 1], sharey=ax)

        # use the previously defined function
        self.plot_hist(data, ax_hist)
        self.plot_scatter(data, ax, lower_limit, upper_limit)

        plt.suptitle(title)
        ax.tick_params(axis='x', labelrotation=45)
        ax.set(xlabel=self.x_data_label, ylabel=self.y_label)
        ax_hist.set(xlabel=self.x_hist_label)

        ax_hist.tick_params(axis='x', labelrotation=45)

        self.figure_index += 1
        self.figures[title] = fig

    @staticmethod
    def show_plots() -> None:
        plt.show()

    def save_plots(self) -> None:
        for key, fig in self.figures.items():
            fig.savefig(f"{key}_fig.png")
