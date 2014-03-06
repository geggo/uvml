uvml
====

Provide vectorized math function (MKL) for numpy

In numpy some of the 'ufuncs', in particular transcedental math operations such es exp, sin, log, do not use optimized implementations. This package provides ufuncs using fast implementations of the Intel VML library, which is part of Intels Math Kernel Library (MKL). 

![benchmark](Add-Exp.png "benchmark result")

Note
----

This is ancient code from 2009.

License
-------

LGPL

(C) Gregor Thalhammer
