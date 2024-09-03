import sys

input=sys.stdin.readline

dic=dict()

temp=input().strip()
ans=[]
for i in temp:
    dic.setdefault(i,0)
    dic[i]+=1
key=sorted(dic.keys())
flag=0
for i in key:
    if dic[i]%2==1:
        if flag!=0:
            print("I'm Sorry Hansoo")
            quit()
        else:
            flag=i
    ans.append(i*(dic[i]//2))
print("".join(ans),end="")
if flag!=0:
    print(flag,end="")
print("".join(reversed(ans)))