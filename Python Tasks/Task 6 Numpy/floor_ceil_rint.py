import numpy
numpy.set_printoptions(sign=' ')
A = numpy.array(list(map(float, input().split())), dtype=float)
print (numpy.floor(A))
print (numpy.ceil(A))
print (numpy.rint(A))