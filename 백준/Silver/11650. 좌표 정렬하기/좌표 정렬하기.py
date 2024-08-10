import sys
input=sys.stdin.readline
print=sys.stdout.write
temp={}
for i in range(int(input())):
    a,b=map(int,input().split())
    temp.setdefault(a,[])
    temp[a].append(b)
temp_keys=sorted(list(temp.keys()))
for i in temp_keys:
    temp_values=sorted(temp[i])
    for k in temp_values:
        print(str(i)+" "+str(k)+"\n")