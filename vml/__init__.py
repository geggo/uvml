"""
Provides fast vector math ufuncs, using Intel's Vector Math Library (VML),
which is part of the Math Kernel Library (MKL)
"""
__version__ = '0.1'

import numpy
from uvml import *

__old_numeric_ops = None
def use_vml(use_vml = True):
    """change numpy so that it uses by default some of the vectorized functions""" 
    if use_vml:
        if __old_numeric_ops is None:
            old_numeric_ops = numpy.set_numeric_ops(
                multiply = Mul,
                divide = Div,
                power = Pow,
                sqrt = Sqrt,
                square = Sqr)
    else:
        if __old_numeric_ops is not None:
            numpy.set_numeric_ops(**old_numeric_ops)

