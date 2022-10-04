import numpy
n,m=map(int,input().split())
ar = []
for i in range(n):
    temp = list(map(int,input().split()))
    ar.append(temp)
np_ar = numpy.array(ar)
s = numpy.sum(np_ar,axis=0)
print(numpy.prod(s))