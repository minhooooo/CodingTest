import sys
input=sys.stdin.readline
print=sys.stdout.write
temp=list()
for _ in range(int(input())):
    temp.append(int(input()))
for i in sorted(temp):
    print(str(i)+"\n")