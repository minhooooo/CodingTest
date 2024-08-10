temp=list()
for _ in range(int(input())):
    temp.append(list(map(int,input().split())))
for i in range(len(temp)):
    count=1
    for k in range(len(temp)):
        if i==k:
            continue
        if temp[k][0]>temp[i][0] and temp[k][1]>temp[i][1]:
            count+=1
    print(count,end=' ')