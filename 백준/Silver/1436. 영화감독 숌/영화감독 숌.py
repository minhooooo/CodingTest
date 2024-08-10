import sys
input=sys.stdin.readline
print=sys.stdout.write
a=int(input())
count=0
now=666
while 1:
    if "666" in str(now):
        count+=1
    if count==a:
        break
    now+=1
print(str(now))