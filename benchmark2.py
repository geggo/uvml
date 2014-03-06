import numpy
import vml
import timeit

from matplotlib import pyplot

#from numexpr import evaluate


setup = """
import vml
import numpy
#from numexpr import evaluate, numexpr
xd = numpy.linspace(0.8,1.2, %d)
od = numpy.ones_like(xd)
yd = numpy.linspace(2,3, %d)
zd = numpy.empty_like(xd)
td = numpy.empty_like(xd)

xf = xd.astype(numpy.float32)
yf = yd.astype(numpy.float32)
zf = numpy.empty_like(xd)

#nexp = numexpr('exp(x)', (('x', float),))
#nexpa = numexpr('sin(x) + cos(y)', (('x', float),('y', float)))
#nsqr = numexpr('x**2', (('x', float),))

expr1 = 'xd*yd + numpy.sin(zd**2)'
expr2 = 'xd*yd + sin(zd**2)'
#nexpr = numexpr(expr2, (('xd', float), ('yd', float), ('zd', float)))
#npexpr = compile(expr1, '<expr>', 'eval')

"""
 
benchmarks = ['vml.Exp(xd,zd)',
              'vml.Add(xd, yd, zd)',
              'numpy.add(xd, yd, zd)',
              #'vml.Ln(xd, yd)',
              #'vml.Mul(xd, yd, zd)',
              #'vml.Inv(xd, zd)',
              #'numpy.divide(xd, yd, zd)',
              #'vml.Div(xd, yd, zd)'
              #'numpy.power(xd, yd, zd)',
              #'vml.Pow(xd, yd, zd)'
              #'vml.Div(1.0, xd, xd)',
              #'vml.Div(od, xd, xd)',
              #'vml.Inv(xd, xd)',
              #'numpy.divide(1.0, xd, xd)',
              #'vml.Round(xd, zd)',
              #'numpy.add(xd, xd, xd)', #lower memory limit
              #'vml.Add(xd, xd, xd)', #lower memory limit
              #'numpy.add(xd, 1.0, xd)',
              #'vml.Add(xd, 1.0, xd)',
              #'vml.Add(xd[::2], yd[::2], zd[::2])',
              #'vml.Add(xd[::2], yd[::2], zd[:len(zd)/2])',
              #'numpy.add(xd[::2], yd[::2], zd[::2])'
              'numpy.exp(xd, yd)',
              #'numpy.power(xd,2.0,zd)',
              #'vml.Pow(xd, 2.0, zd)',
              #'vml.Erf(xd, yd)',
              #'numpy.sin(xd, zd)',
              #'vml.Sin(xd, zd)',
              #"evaluate('xd')",
              #"vml.Add(xd, yd)",
              #'xd*yd + 1.0/yd',
              #"evaluate('sin(xd)')",
              #"evaluate('cos(xd)')",
              #'vml.Sin(xd,zd)',
              #'numpy.sin(xd,zd)',
              #'vml.Mul(xd,yd,zd);vml.Inv(yd,td);vml.Add(zd,td,zd)',
              #    
              #'numpy.exp(xd, zd)',
              #"evaluate('exp(xd)')",
              #'nexp(xd)',
              #'vml.Exp(xd)',
              #'vml.Exp(xd,zd)', #prereserving output saves a lot!
              #
              #'numpy.add(numpy.sin(xd), numpy.cos(xd))', #with one thread, keep full speed nexpr
              #'vml.Add(vml.Sin(xd), vml.Cos(yd))',
              #'nexpa(xd,yd)',
              #
              #'vml.Sqr(xd[::2], yd[::2])', #copying cuts memory bound performance by 2
              #'vml.Sqr(xd[::2], yd[:len(yd)/2])', #only copying input 
              #'numpy.square(xd[::2], yd[::2])',
              #'numpy.square(xd[::2], yd[:len(yd)/2])',
              #'vml.Sqr(xd[::2])',
              #'nsqr(xd[::2])',
              #
              #compare single and double precision
              #'numpy.sin(xd, yd)',
              #'numpy.sin(xf, yf)',
              #'vml.Sin(xd, yd)',
              #'vml.Sin(xf, yf)', #single precision vml sin is fast!
              #
              #'numpy.square(xd,yd)', #at large size memory bound, single double performance
              #'numpy.square(xf,yf)', #at medium size numpy single and double the same
              #'nsqr(xd)',
              #'vml.Sqr(xd, yd)',
              #'vml.Sqr(xf, yf)',
              #
              #'nexpr(xd,yd,zd)',
              #'eval(npexpr)',
              ]

Nvecs = numpy.logspace(2,6.0, 41).astype(numpy.int)
Nvecs = Nvecs/2 * 2
cyc = numpy.zeros((len(Nvecs), len(benchmarks)))
    
for row, Nvec in enumerate(Nvecs):
    for col, stmt in enumerate(benchmarks):
        t = timeit.Timer(stmt = stmt, setup = setup%(Nvec, Nvec))
        reps = max(1, int(round(1e6/Nvec)))
        clks = min(t.repeat(3, number = reps))*1.8e9/(Nvec*reps)
        print "%8d %5d"%(Nvec, reps),
        print "%20s"%stmt,
        print "%6.2f"%(min(t.repeat(3, number = reps))*1.8e9/(Nvec*reps) )
        cyc[row, col] = clks

for k, stmt in enumerate(benchmarks):
    pyplot.loglog(Nvecs, cyc[:,k], '.-', label = stmt)

pyplot.legend(loc=0)
pyplot.show()
