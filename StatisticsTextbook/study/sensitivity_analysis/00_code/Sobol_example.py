from SALib.sample import saltelli, latin
import SALib.sample.morris as sample_morris

from SALib.analyze import sobol
from SALib.test_functions import Ishigami

if __name__ == "__main__":
    problem = {
        'num_vars': 3,
        'names': ['x1', 'x2', 'x3'],
        'bounds': [[-3.14159265359, 3.14159265359],
                   [-3.14159265359, 3.14159265359],
                   [-3.14159265359, 3.14159265359]]
    }

    # saltelli sampling and sobol analyze
    # sobol_sample = sobol_sequence.sample(problem, 1000) # not callable
    print("saltelli sampling")
    param_values = saltelli.sample(problem, 1000)
    print(param_values.shape)
    saltelli_return = Ishigami.evaluate(param_values)
    Si_sobol = sobol.analyze(problem, saltelli_return)

    print(Si_sobol['S1'])
    print(Si_sobol['ST'])
    print(f"x1-x2: {Si_sobol['S2'][0, 1]}")
    print(f"x1-x3: {Si_sobol['S2'][0, 2]}")
    print(f"x2-x3: {Si_sobol['S2'][1, 2]}")
    Si_sobol.plot()
    print()

    print("latin sampling")
    latin_sample = latin.sample(problem, 1000)
    print(latin_sample.shape)
    latin_return = Ishigami.evaluate(latin_sample)
    Si_sobol = sobol.analyze(problem, latin_return)

    print(Si_sobol['S1'])
    print(Si_sobol['ST'])
    print(f"x1-x2: {Si_sobol['S2'][0, 1]}")
    print(f"x1-x3: {Si_sobol['S2'][0, 2]}")
    print(f"x2-x3: {Si_sobol['S2'][1, 2]}")
    Si_sobol.plot()
    print()

    print("morris sampling")
    morris_sample = sample_morris.sample(problem, 2000, num_levels=4)
    morris_return = Ishigami.evaluate(morris_sample)
    Si_sobol = sobol.analyze(problem, morris_return)

    print(Si_sobol['S1'])
    print(Si_sobol['ST'])
    print(f"x1-x2: {Si_sobol['S2'][0, 1]}")
    print(f"x1-x3: {Si_sobol['S2'][0, 2]}")
    print(f"x2-x3: {Si_sobol['S2'][1, 2]}")
    Si_sobol.plot()
    print(morris_sample.shape)
    print()
