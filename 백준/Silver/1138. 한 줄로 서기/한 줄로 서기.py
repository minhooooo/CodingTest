import sys

input=sys.stdin.readline

n = int(input())
temp = list(map(int, input().split()))

result = [0]*n

for i in range(1, n+1):
    cnt = 0
    val = temp[i-1]
    for j in range(n):
        if cnt == val and result[j] == 0:
            result[j] = i
            break
        elif result[j] == 0:
            cnt += 1
for i in result:
    print(i,end=' ')