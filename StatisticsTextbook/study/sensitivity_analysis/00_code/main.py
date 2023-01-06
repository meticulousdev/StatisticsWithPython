from SALib.sample import saltelli
from SALib.analyze import sobol
from SALib.test_functions import Ishigami

import numpy as np
import math


def evaluate(values):
    y = np.zeros([values.shape[0]])
    for i, p in enumerate(values):
        y[i] = test_func(p)
    return y


def test_func(p):
    x = 1
    y = p[2] * x ** 2 + p[1] * x + p[0]
    return y


if __name__ == "__main__":
    names = ['x1', 'x2', 'x3']
    problem = {
        'num_vars': 3,
        'names': names,
        'bounds': [[-3.14159265359, 3.14159265359],
                   [-3.14159265359, 3.14159265359],
                   [-3.14159265359, 3.14159265359]]
    }

    # saltelli sampling and sobol analyze
    # sobol_sample = sobol_sequence.sample(problem, 1000) # not callable
    print("saltelli sampling")
    saltelli_sample = saltelli.sample(problem, 1000)
    print(saltelli_sample.shape)
    saltelli_return = Ishigami.evaluate(saltelli_sample)
    # saltelli_return = evaluate(saltelli_sample)
    Si_sobol = sobol.analyze(problem, saltelli_return)

    print(f"Si     : {Si_sobol['S1']}")
    print(f"ST     : {Si_sobol['ST']}")
    print(f"x1-x2  : {Si_sobol['S2'][0, 1]}")
    print(f"x1-x3  : {Si_sobol['S2'][0, 2]}")
    print(f"x2-x3  : {Si_sobol['S2'][1, 2]}")

    Si_sum = sum(Si_sobol['S1'])
    for Sij_sobol in Si_sobol['S2']:
        for Sij in Sij_sobol:
            if math.isnan(Sij) is not True:
                Si_sum += Sij

    print(f"Si SUM : {Si_sum}")
    print(f"ST SUM : {sum(Si_sobol['ST'])}")

    Si_sobol.plot()
    print()
