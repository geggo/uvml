import numpy
import umkl
import time

x = numpy.linspace(0,3.0, 4)
xd = x.astype(numpy.float64)
xf = x.astype(numpy.float32)
xc = x.astype(numpy.complex128)
yd = numpy.empty_like(xd)
yf = numpy.empty_like(xf)

print "xd: ", xd

print umkl.Exp(xd)
print umkl.Exp(xf)

umkl.NopUnary(xd, yd)
umkl.NopUnary(1.0)
umkl.NopUnary(xf)

umkl.NopBinary(xd, yd)
umkl.NopBinary(xf, yf)
umkl.NopBinary(xd, 1.0)

umkl.NopUnary(xd[::2])
umkl.NopUnary(xd[::-2])

print umkl.Exp(xd[::2])
print umkl.Exp(xd[::-2])
print umkl.Exp(xd[0])

umkl.Add(xd, xd, yd)
print xd[::2], xd[::-2]
print umkl.Add(xd[::2], xd[::-2])
print umkl.Add(xd, 1.0)

print umkl.Mul(xd, 0.0, yd)
print umkl.Add(xd[::2], 1.0, yd[::-2])
print yd

print umkl.cExp(xc)
print umkl.cExp(xc[::2])

