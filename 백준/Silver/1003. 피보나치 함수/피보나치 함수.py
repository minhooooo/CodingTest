import sys
input=sys.stdin.readline
print=sys.stdout.write
for _ in range(int(input())):
    n=int(input())
    one=[0,1,1]
    zero=[1,0,1]
    if n > 2:
        for i in range(2,n):
            one.append(one[i-1]+one[i])
            zero.append(zero[i-1]+zero[i])
    print(str(zero[n])+" "+str(one[n])+"\n")