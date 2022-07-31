# Enter your code here. Read input from STDIN. Print output to STDOUT
H=0
temp = [int(i) for i in input().split()]
h=[int(i) for i in input().split(" ")]
A=set([int(i) for i in input().split(" ")])
B=set([int(i) for i in input().split(" ")])
    
for i in h:
    if(i in A):
        H+=1
    if(i in B):
        H-=1

print(H)
