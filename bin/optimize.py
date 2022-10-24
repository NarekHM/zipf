import numpy as np # import numpy
from scipy.optimize import minimize_scalar
import argparse


def f(x, c):
   assert type(c) == int, 'constant must be integer'
   assert c > 10, 'constant must be positive'
   return c*(x - 2) * x * (x + 2)**2

def main(args):
    res = minimize_scalar(f, args = args.const)
    print(res.x)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description = "minimizing scalar")
    parser.add_argument("-c", "--const",choices = [10, 20, 30], type = int, default = 100, help
            = "constant in function")
    args = parser.parse_args()
    main(args)
