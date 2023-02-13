# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html
import numpy as np
import pandas as pd
from scipy.optimize import least_squares
import matplotlib.pyplot as plt


def gen_data(t, a, b, c, noise=0, n_outliers=0, random_state=0):
    y = a + b * np.exp(t * c)

    rnd = np.random.RandomState(random_state)
    error = noise * rnd.randn(t.size)
    outliers = rnd.randint(0, t.size, n_outliers)
    error[outliers] *= 10

    return y + error


def fun(x, t, y):
    return x[0] + x[1] * np.exp(x[2] * t) - y


if __name__ == "__main__":
    a = 0.5
    b = 2.0
    c = -1
    t_min = 0
    t_max = 10
    n_points = 15

    t_train = np.linspace(t_min, t_max, n_points)
    y_train = gen_data(t_train, a, b, c, noise=0.1, n_outliers=3)

    x0 = np.array([1.0, 1.0, 0.0])
    res_lsq = least_squares(fun, x0, args=(t_train, y_train))
    res_soft_l1 = least_squares(fun, x0, loss='soft_l1', f_scale=0.1,
                                args=(t_train, y_train))
    res_log = least_squares(fun, x0, loss='cauchy', f_scale=0.1,
                            args=(t_train, y_train))
