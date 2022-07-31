# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(map(int, input().split()))
res = []
for i in range(int(input())):
     res.append(a.issuperset(set(map(int,input().split())))) #a.issuperset(b)
print(all(res)) #prints True only if all elements in the list are True
