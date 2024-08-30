import sys
from collections import deque 
input=sys.stdin.readline

n=int(input())
node=dict()

for _ in range(n):
    a,b,c=input().strip().split()
    node[a]=[b,c]

first=[]
last=[]
mid_stack=[]

def fi(no):
    first.append(no)
    for i in node[no]:
        if i=='.':
            continue
        fi(i)

def mi(no):
    if node[no][0]!='.':
        mi(node[no][0])
    mid_stack.append(no)
    if node[no][1]!='.': 
        mi(node[no][1])

def la(no):
    if node[no][0]!='.':
        la(node[no][0])
    if node[no][1]!='.': 
        la(node[no][1])
    last.append(no)


fi('A')
print(''.join(first))
mi('A')
print(''.join(mid_stack))
la('A')
print(''.join(last))