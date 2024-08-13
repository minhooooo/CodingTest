import sys
input=sys.stdin.readline
print=sys.stdout.write
a=int(input())
temp=list(map(int,input().split()))
temp_set=set(temp)
temp_dic=dict()
result=dict()
for i in temp_set:
    temp_dic.setdefault(i,0)
    temp_dic[i]+=1
key=sorted(list(temp_dic.keys()))
for i in range(len(key)):
    if i==0:
        result[key[i]]=0
    else:
        result[key[i]]=temp_dic[key[i-1]]+result[key[i-1]]
for i in temp:
    print(str(result[i])+" ")
