from six_sigma.calc import mean
from random import random, gauss
from six_sigma.calc import mean,stddev
from six_sigma.plot import create_plot, create_histogramm

test_data = [min(random() * 100,100) for _ in range(1000)]
test_data_gaus = [min(gauss(mu=90, sigma=10),100) for _ in range(100)]
test_data_gaus.append(50)
test_data_gaus.append(55)
test_data_gaus.append(59)

create_plot(test_data_gaus,lower_limit=80,dataset_name="12345-ps")
create_histogramm(test_data_gaus,lower_limit=80,dataset_name="12345-ps")
