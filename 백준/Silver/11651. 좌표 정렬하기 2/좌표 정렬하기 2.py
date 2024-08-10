temp=dict()
for _ in range(int(input())):
    a,b=map(int,input().split())
    temp.setdefault(b,[])
    temp[b].append(a)
for i in sorted(temp.keys()):
    for k in sorted(temp[i]):
        print(k,i)