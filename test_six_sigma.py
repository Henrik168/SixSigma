from six_sigma.calc import mean
from random import random, gauss, randrange
from six_sigma.calc import mean, stddev
from six_sigma.plot import Plot

test_data = [randrange(50, 80) for _ in range(1000)]
test_data_gaus = [min(gauss(mu=97, sigma=2), 100) for _ in range(1000)]
test_data_gaus2 = [min(gauss(mu=90, sigma=10), 100) for _ in range(1000)]

plt = Plot(y_label="Y-Label",
           x_data_label="X-Data",
           x_hist_label="X-Hist",
           y_min=0,
           y_max=100)
plt.add_plot(test_data_gaus, "GausData1", 100, 80)
plt.add_plot(test_data_gaus2, "GausData2", 100, 80)
plt.add_plot(test_data, "RandData", 75, 55)
#plt.show_plots()
plt.save_plots()
