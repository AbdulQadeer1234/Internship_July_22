# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
s1 = set(map(int, input().split()))
N = int(input())

for i in range(N):
    cmd,i = input().split()
    s2 = set(map(int, input().split()))
    if(cmd == "intersection_update"):
        s1.intersection_update(s2)
    elif(cmd == "update"):
        s1.update(s2)
    elif(cmd == "symmetric_difference_update"):
        s1.symmetric_difference_update(s2)
    elif(cmd == "difference_update"):
        s1.difference_update(s2)

print(sum(s1))
