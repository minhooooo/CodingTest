x,y=map(int,input().split())
temp=list()
for _ in range(x):
    temp.append(list(input()))
min=64
for i in range(x-7):
    for j in range(y-7):
        count=0
        for p in range(8):
            for q in range(8):
                if (p+q)%2==0:
                    if temp[i+p][j+q]=='W':
                        count+=1
                else:
                    if temp[i+p][j+q]=='B':
                        count+=1      
        if min>=count:
            min=count
        if min>64-count:
            min=64-count
print(min)