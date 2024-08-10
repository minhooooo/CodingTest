import math

num=int(input())
size=list(map(int,input().split()))
tp=list(map(int,input().split()))
count=0
for i in size:
    count=count+math.ceil(i/tp[0])
print(count)
print(num//tp[1],num%tp[1])