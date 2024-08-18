import sys

input=sys.stdin.readline

M,N=map(int,input().split())
site_dic=dict()

for _ in range(M):
    site,pw=map(str,input().strip().split())
    site_dic[site]=pw
for _ in range(N):
    print(site_dic[input().strip()])
