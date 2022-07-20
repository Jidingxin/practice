import baostock as bs
import pandas as pd

import numpy as np

import scipy.stats as stats
import scipy.optimize as opt

rv_unif = stats.uniform.rvs(size=10)
print(rv_unif)
rv_beta = stats.beta.rvs(size=10, a=4, b=2)
print(rv_beta)
