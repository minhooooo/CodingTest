import sys

N,M=map(int,input().strip().split())
name_dic=dict()
num_dic=dict()
for i in range(1,N+1):
    temp=input()
    name_dic[temp]=i
    num_dic[i]=temp
for _ in range(M):
    temp=input()
    if temp.isdigit() :
        print(num_dic[int(temp)])
    else:
        print(name_dic[temp])