#!/usr/bin/env python3
"""
Calls a given function with specified values, and prints the result to output
"""


from mypackage.utils import math


def _parse_cmd_opts():
    """Parses command line options"""
    import argparse
    parser = argparse.ArgumentParser(description="Do math on some numbers")
    parser.add_argument("-f", dest="function", required=True)
    parser.add_argument("vals", nargs="+", type=float)
    return parser.parse_args()


def main():
    """Calls the function given in cli options with specified values"""
    opts = _parse_cmd_opts()
    if hasattr(math, opts.function):
        result = getattr(math, opts.function)(*opts.vals)
        print(result)
    else:
        raise KeyError("function {} is not defined".format(opts.function))


if __name__ == '__main__':
    main()
