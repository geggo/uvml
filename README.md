uvml
====

Provide vectorized math function (MKL) for numpy

In numpy some of the 'ufuncs', in particular transcedental math operations such es exp, sin, log, do not use optimized implementations. This package provides ufuncs using fast implementations of the Intel VML library, which is part of Intels Math Kernel Library (MKL).

A better approach than this package is using numexpr, numba or theano. However, using `numpy.set_numeric_ops`  you can replace some of the internal numpy ufuncs with optimized ones (a shortcut is provided by vml.use_vml(True) ). By this you can gain some speed improvements without changing your code.


![benchmark](Add-Exp.png "benchmark result")

This benchmark (on an ancient Intel Core2Duo CPU) demonstrates the speed gain that can be achieved with this package. Shown is the execution time (in CPU cycles) for various array sizes. For 'exp' a speed gain up to 5x - 10x can be achieved. Around array size of 10^4 both cores are used, above array sizes of 10^5 the data is too large to fit into the cache. 

For basic operations such as addition or multiplication compilers produce optimized code, so no speed gain. For optimum performance keeping the data in cache is crucial, therefor approaches like numexpr, numba or theano will likely perform faster for composite expressions. 

Note
----

This is ancient code from 2009.

License
-------

LGPL

(C) Gregor Thalhammer
