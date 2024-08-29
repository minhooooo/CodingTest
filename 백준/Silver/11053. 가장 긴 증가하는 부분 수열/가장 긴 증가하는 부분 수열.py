import itertools

n=int(input())

arr=list(map(int,input().strip().split()))

temp=[1]*n

for i in range(len(arr)):
    for k in range(i):
        if arr[k]<arr[i] :
            temp[i]=max(temp[i],temp[k]+1)
print(max(temp))