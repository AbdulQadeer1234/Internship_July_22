import numpy
N,M = map(int, input().split())
l = []
for i in range(N):
    a = list(map(int, input().split()))
    l.append(a)
l = numpy.array(l)

print(numpy.mean(l, axis = 1))
print(numpy.var(l, axis = 0))
print(round(numpy.std(l),11))
