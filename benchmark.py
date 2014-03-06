import numpy
import umkl
import timeit

Nvec = 10000
repetitions = 100

setup = """
import umkl
import numpy
xd = numpy.linspace(0.8,1.2, %d)
yd = numpy.empty_like(xd)
zd = numpy.empty_like(xd)
od = numpy.ones_like(xd)

xf = xd.astype(numpy.float32) 
yf = numpy.empty_like(xf)
zf = numpy.empty_like(xf)
of = numpy.ones_like(xf)
"""%Nvec

benchmarks = [#'umkl.Exp2(xd,yd)',
              'umkl.Exp(xd,yd)',
              'umkl.Exp(xf,yf)',
              #'umkl.Expm1(xd, yd)', #slow
              #'umkl.Expm1(xf, yf)', #slow
              'umkl.Ln(xd, yd)',
              'umkl.Ln(xf, yf)',
              #'umkl.Log1p(xd, yd)', #slow
              #'umkl.Log1p(xf, yf)', #slow
              'umkl.Sin(xd,yd)',
              'umkl.Sin(xf,yf)',
              'umkl.Abs(xd, yd)',
              'umkl.Inv(xd, yd)',
              'pass',
              'umkl.Add(xd, yd, zd)',
              'umkl.Add(xf, yf, zf)',
              'umkl.Sub(xd, yd, zd)',
              'umkl.Sub(xf, yf, zf)',
              'umkl.Mul(xd, yd, zd)',
              'umkl.Mul(xf, yf, zf)',
              'pass',
              'numpy.exp(xd,yd)', #slow
              'numpy.expm1(xd, yd)',
              #'numpy.exp(xf,yf)', #slow
              'numpy.add(xd,yd,zd)',
              'numpy.add(xf,yf,zf)',
              'pass',
              #'umkl.Mul2(xd, yd)',
              'umkl.Add(xd, 1.0, zd)',
              'umkl.Add(xf, 1.0, zf)',
              #'umkl.Add(xd, od, zd)',
              #'umkl.Add(xf, of, zf)',
              'numpy.add(xd, 1.0, zd)',
              'numpy.add(xf, 1.0, zf)',
              'numpy.sum(xd)',
              'umkl.Exp(xd[::2])',
              'numpy.exp(xd[::2])',
              'numpy.power(xd, 2.0)',
              'umkl.Pow(xd, 2.0)',
              #'umkl.Nop(xd, yd)',
              ]


for stmt in benchmarks:
    t = timeit.Timer(stmt = stmt, setup = setup)
    print "%20s"%stmt,
    print "%6.2f"%(min(t.repeat(3, number = repetitions))*1.8e9/(Nvec*repetitions) )
