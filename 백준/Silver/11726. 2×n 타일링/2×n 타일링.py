import sys
input=sys.stdin.readline
print=sys.stdout.write
a=int(input())
temp=[1,2]
if a>2:
    for i in range(2,a):
        temp.append(temp[i-1]+temp[i-2])
print(str(temp[a-1]%10007)+"\n")