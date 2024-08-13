import sys
input=sys.stdin.readline
print=sys.stdout.write
import heapq
test=int(input())
temp=[]
len=0
for _ in range(test):
    num=int(input())
    if num==0:
        if len==0:
            print("0\n")
        else:
            print(str(heapq.heappop(temp))+"\n")
            len-=1
    else:
        heapq.heappush(temp,num)
        len+=1