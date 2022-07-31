if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    m=max(arr)
    for i in range(0,arr.count(m)):
        arr.remove(m)
    print(max(arr))
        
