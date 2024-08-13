import sys
input=sys.stdin.readline
print=sys.stdout.write
computers=int(input())
pair=int(input())
virus=set([1])
connections=[]

for _ in range(pair):
    a, b = map(int, input().split())
    connections.append((a, b))

added=1
while added:
    added=0
    for a, b in connections:
        if a in virus and b not in virus:
            virus.add(b)
            added = 1
        elif b in virus and a not in virus:
            virus.add(a)
            added = 1
print(str(len(virus) - 1) + "\n")