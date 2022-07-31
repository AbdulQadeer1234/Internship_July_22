if __name__ == '__main__':
    l1=[]
    l2=[]
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    for i in range(0,x+1):
      for j in range(0,y+1):
        for k in range(0,z+1):
          l1.append([i,j,k])
          if(sum(l1[0])<n or sum(l1[0])>n):
            l2.append(l1[0])
          l1.clear()
    print(l2)
