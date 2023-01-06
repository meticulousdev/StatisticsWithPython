from SALib.sample import fast_sampler, saltelli, latin
import SALib.sample.morris as sample_morris
import matplotlib.pyplot as plt

from SALib.analyze import fast, sobol, morris, rbd_fast
from SALib.test_functions import Ishigami

import numpy as np


def Ishigami_equation(x1, x2, x3):
    A = 7
    B = 0.1

    ret = np.sin(x1) + A * ((np.sin(x2)) ** 2) + B * (x3 ** 3) * np.sin(x1)
    return ret


if __name__ == "__main__":
    problem = {
        'num_vars': 3,
        'names': ['x1', 'x2', 'x3'],
        'bounds': [[-3.14159265359, 3.14159265359],
                   [-3.14159265359, 3.14159265359],
                   [-3.14159265359, 3.14159265359]]
    }

    np.set_printoptions(precision=3, suppress=True)

    print("Sobol Sensitivity Analysis")
    param_values = saltelli.sample(problem, 512)
    saltelli_return = Ishigami.evaluate(param_values)
    Si_sobol = sobol.analyze(problem, saltelli_return)

    print(f"Si : {Si_sobol['S1']}")
    print(f"ST : {Si_sobol['ST']}")
    print(f"x1-x2: {Si_sobol['S2'][0, 1]:.3f}")
    print(f"x1-x3: {Si_sobol['S2'][0, 2]:.3f}")
    print(f"x2-x3: {Si_sobol['S2'][1, 2]:.3f}")
    print()

    print("FAST - Fourier Amplitude Sensitivity Test")
    X = fast_sampler.sample(problem, 1000)
    Y = Ishigami.evaluate(X)
    Si_fast = fast.analyze(problem, Y, print_to_console=False)

    # List to np.ndarray
    print(f"Si : {np.asarray(Si_fast['S1'])}")
    print(f"ST : {np.asarray(Si_fast['ST'])}")
    print()

    print("Morris")
    X = sample_morris.sample(problem, 1000, num_levels=4)
    Y = Ishigami.evaluate(X)
    Si_morris = morris.analyze(problem, X, Y, conf_level=0.95,
                               print_to_console=False, num_levels=4)
    print(f"Mu*   : {np.asarray(Si_morris['mu_star'])}")
    print(f"Mu    : {np.asarray(Si_morris['mu'])}")
    print(f"sigma : {np.asarray(Si_morris['sigma'])}")
    print()

    n_size = 100
    x1_vec = np.linspace(-np.pi, np.pi, n_size)
    x2_vec = np.linspace(-np.pi, np.pi, n_size)
    x3_vec = np.linspace(-np.pi, np.pi, n_size)

    X1, X2, X3 = np.meshgrid(x1_vec, x2_vec, x3_vec)
    Z = np.zeros([n_size, n_size, n_size])
    for i, x1 in enumerate(x1_vec):
        for j, x2 in enumerate(x2_vec):
            for k, x3 in enumerate(x3_vec):
                Z[i, j, k] = Ishigami_equation(x1, x2, x3)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    pnt3d = ax.scatter(X1, X2, X3, c=Z)
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('x3')
    plt.show()
    plt.colorbar(pnt3d)
    plt.show()
    print()

