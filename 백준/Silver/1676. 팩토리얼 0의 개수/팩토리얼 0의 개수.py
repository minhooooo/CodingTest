count=int(input())
temp=1
result=0
for i in range(1,count+1):
    temp=temp*i
for i in reversed(list(str(temp))):
    if i=='0':
        result+=1
    else:
        print(result)
        break
    