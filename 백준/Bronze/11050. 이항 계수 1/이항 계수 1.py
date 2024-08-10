a,b=map(int,input().split())
temp=1
for i in range(b):
    temp=temp*(a-i)
for i in range(1,b+1):
    temp=temp/i
print(int(temp))