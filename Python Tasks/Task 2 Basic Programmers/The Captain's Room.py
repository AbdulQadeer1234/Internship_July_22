# Enter your code here. Read input from STDIN. Print output to STDOUT
k=int(input())
l=list(map(int,input().split()))
s=set(l)
print(int((sum(s)*k-(sum(l)))/(k-1)))
#sum(s)*k gives us sum of (room no: * k) = 1*5 + 2*5 + 3*5 + 4*5 + 5*5 + 6*5 + 8*5
#sum(l) gives us the actual sum of the given room no: = 1*5 + 2*5 + 3*5 + 4*5 + 5*5 + 6*5 + 8*(1)
#if we subtract these two values we get 
#after cancelling common terms as 8*5 - 8*(1) = 8*4
#so we devide by k-1 i.e '4' to get the required ans..
