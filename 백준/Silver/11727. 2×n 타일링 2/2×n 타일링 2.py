import sys
import math

input=sys.stdin.readline

result=[0,1,3,5,11]
n=int(input())
if n>=5:
    for i in range(5,n+1):
        result.append(result[i-2]*2+result[i-1])
print(result[n]%10007)