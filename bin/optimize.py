import numpy as np # importing numpy 
from scipy.optimize import minimize_scalar
import argparse


def f(x, c):

   return c*(x - 2) * x * (x + 2)**2

def main(args):
    res = minimize_scalar(f, args = args.const)
    print(res.x)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description = "minimizing scalar")
    parser.add_argument("-c", "--const", type = int, default = 100, help
            = "constant in function")
    args = parser.parse_args()
    main(args)
