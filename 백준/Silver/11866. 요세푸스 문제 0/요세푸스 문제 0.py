import sys
input=sys.stdin.readline
print=sys.stdout.write
a,b=map(int,input().split())
temp=[]
count=0
answer=[]
for i in range(a):
    temp.append(i+1)
while(len(temp)>0):
    count=(count+b-1)%len(temp)
    answer.append(temp.pop(count))
for i in range(len(answer)):
    if i ==0:
        print("<"+str(answer[i]))
    elif i<len(answer)-1:
        print(", "+str(answer[i]))
    else :
        print(", "+str(answer[i]))
print(">")