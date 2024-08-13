import sys
input=sys.stdin.readline
print=sys.stdout.write
n=int(input())
count=[0]*11
for _ in range(n):
    temp=int(input())
    for i in range(1,temp+1):
        if i==1:
            count[i]=1
        elif i==2:
            count[i]=2
        elif i==3:
            count[i]=4
        else:
            count[i]=count[i-1]+count[i-2]+count[i-3]
    print(str(count[temp])+"\n")