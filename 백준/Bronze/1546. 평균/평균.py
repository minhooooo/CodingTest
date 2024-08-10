count=int(input())
temp=list(map(int,input().split()))
maxs=max(temp)
for i in range(count):
    temp[i]=temp[i]*100/maxs
print(sum(temp)/count)