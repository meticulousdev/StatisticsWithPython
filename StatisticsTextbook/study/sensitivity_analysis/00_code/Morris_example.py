import SALib.sample.morris as sample_morris

from SALib.analyze import sobol, morris, rbd_fast
from SALib.test_functions import Ishigami

if __name__ == "__main__":
    problem = {
        'num_vars': 3,
        'names': ['x1', 'x2', 'x3'],
        'bounds': [[-3.14159265359, 3.14159265359],
                   [-3.14159265359, 3.14159265359],
                   [-3.14159265359, 3.14159265359]]
    }

    # morris sampling and morris analyze
    X = sample_morris.sample(problem, 1000, num_levels=4)
    Y = Ishigami.evaluate(X)
    Si_morris = morris.analyze(problem, X, Y, conf_level=0.95,
                               print_to_console=True, num_levels=4)
    print()
