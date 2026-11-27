def prefix(arr):
    n = len(arr)
    p = [0]*n
    if n ==0:
        return p
    p[0] = arr[0]
    for i in range(1,n):
        p[i] = p[i-1]+arr[i]
    return p
arr = list(map(int, input().split())) 
print(prefix(arr))  
