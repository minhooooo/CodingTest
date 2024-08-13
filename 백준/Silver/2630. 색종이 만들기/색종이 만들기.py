import sys
input=sys.stdin.readline
print=sys.stdout.write
n=int(input())
temp=[]
result=[]
for _ in range(n):
    temp.append(list(map(int,input().split())))
def search(x,y,n):
    target=temp[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if target!=temp[i][j]:
                search(x,y,n//2)
                search(x,y+n//2,n//2)
                search(x+n//2,y,n//2)
                search(x+n//2,y+n//2,n//2)
                return
    if target==0:
        result.append(0)
    else:
        result.append(1)
search(0,0,n)
print(str(result.count(0))+" "+str(result.count(1)))