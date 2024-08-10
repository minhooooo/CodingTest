a=int(input())
result=1
for i in range(a//5,-1,-1):
    if (a-(i*5))%3==0:
        print((a-(i*5))//3+i)
        result=0
        break
if result:
    print(-1)