from random import gauss, randrange, seed
from six_sigma.plot import Plot

seed(42)
test_data = [randrange(50, 80) for _ in range(1000)]
test_data_gauss = [min(gauss(mu=97, sigma=2), 100) for _ in range(1000)]
test_data_gauss2 = [min(gauss(mu=90, sigma=10), 100) for _ in range(1000)]

plt = Plot(y_label="Y-Label",
           x_data_label="X-Data",
           x_hist_label="X-Hist",
           y_min=0,
           y_max=100,
           bin_width=2)

plt.add_plot(test_data_gauss, "GaussData1", 100, 80)
plt.add_plot(test_data_gauss2, "GaussData2", 100, 80)
plt.add_plot(test_data, "RandData", 75, 55)
plt.show_plots()
plt.save_plots()
