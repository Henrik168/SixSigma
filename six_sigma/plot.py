#Global Libraries
import matplotlib.pyplot as plt
from typing import Tuple
from os import path
#Local Libraries
from six_sigma.calc import mean, stddev, median


class Plot:
    def __init__(self,
                 y_label: str = None,
                 x_data_label: str = None,
                 x_hist_label: str = None,
                 y_min: float = None,
                 y_max: float = None,
                 bin_width: int = 1):
        self._figure_index: int = 1
        self._figures = dict()
        self._y_label = y_label
        self._x_data_label = x_data_label
        self._x_hist_label = x_hist_label
        self._y_min = y_min
        self._y_max = y_max
        self._bin_width = bin_width

    def _min(self, data) -> float:
        return self._y_min if self._y_min is not None else min(data)

    def _max(self, data) -> float:
        return self._y_max if self._y_max is not None else max(data)

    @staticmethod
    def _calc_sigma(data: list) -> Tuple:
        median_value = median(data)
        mean_value = mean(data)
        stddev_value = stddev(data)
        upper_3s = min((mean_value + 3 * stddev_value), 100)
        lower_3s = max((mean_value - 3 * stddev_value), 0)
        return median_value, mean_value, stddev_value, lower_3s, upper_3s

    @staticmethod
    def _in_bounds(lower, value, upper) -> bool:
        return lower <= value <= upper

    def _plot_labels(self, ax, ax_hist, title):
        plt.suptitle(title)
        handles, _ = ax.get_legend_handles_labels()
        ax.legend(handles=handles)
        ax.set(xlabel=self._x_data_label, ylabel=self._y_label)
        ax_hist.set(xlabel=self._x_hist_label)
        ax_hist.tick_params(axis="x", labelrotation=45)
        ax.tick_params(axis="x", labelrotation=45)

    @staticmethod
    def _plot_statistics(ax, mean_value: float, lower_3s: float, upper_3s: float,
                         upper_limit: float, lower_limit: float) -> None:
        ax.axhline(y=mean_value, color="blue", linestyle="-.", label="Mean Value")
        ax.axhline(y=upper_3s, color="orange", linestyle="--", label="3 Sigma")
        ax.axhline(y=lower_3s, color="orange", linestyle="--")
        ax.axhline(y=upper_limit, color="red", linestyle="-", label="Limit")
        ax.axhline(y=lower_limit, color="red", linestyle="-")

    def _plot_hist(self, data, ax_hist, bin_width) -> None:
        ax_hist.tick_params(axis="y", labelleft=False)

        scale_min = int(self._min(data))
        scale_max = (int(self._max(data) / bin_width) + 1) * bin_width

        bins = [bin_element for bin_element in range(scale_min, scale_max, bin_width)]
        ax_hist.hist(data, bins=bins, orientation="horizontal")

    def _plot_scatter(self, data, ax, lower_limit, upper_limit) -> None:
        for index, value in enumerate(data):
            if not self._in_bounds(lower_limit, value, upper_limit):
                ax.plot(index, value, "ro")
                continue
            ax.plot(index, value, "go")

    def add_plot(self, data: list, title: str, upper_limit: float, lower_limit: float) -> None:
        if title in self._figures.keys():
            raise KeyError(f"This Plot: '{title}' already exists")

        median_value, mean_value, stddev_value, lower_3s, upper_3s = self._calc_sigma(data)

        fig = plt.figure(num=self._figure_index, figsize=[10, 7])
        gs = fig.add_gridspec(nrows=1, ncols=2,
                              width_ratios=(7, 3),
                              wspace=0.1)

        ax = fig.add_subplot(gs[0, 0])
        ax.axis([0, len(data), self._min(data), self._max(data)])
        ax_hist = fig.add_subplot(gs[0, 1], sharey=ax)

        self._plot_hist(data, ax_hist, self._bin_width)
        self._plot_scatter(data, ax, lower_limit, upper_limit)
        self._plot_statistics(ax, mean_value, lower_3s, upper_3s,
                              upper_limit, lower_limit)
        self._plot_labels(ax, ax_hist, title)

        self._figures[title] = fig
        self._figure_index += 1

    @staticmethod
    def show_plots() -> None:
        plt.show()

    def save_plots(self, dir_path: str = "./") -> None:
        for key, fig in self._figures.items():
            file_name = f"{key}_fig.png"
            fig.savefig(path.join(dir_path, file_name))
