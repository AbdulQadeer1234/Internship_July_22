import numpy
m, n = map(int, input().split())
a = numpy.array([list(map(int, input().split())) for i in range(m)], numpy.int64)
b = numpy.array([list(map(int, input().split())) for i in range(m)], numpy.int64)
print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(numpy.floor_divide(a,b))
print(numpy.mod(a,b))
print(numpy.power(a,b))
