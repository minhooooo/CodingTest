import itertools

n,m=map(int,input().strip().split())

arr=[i for i in range(1,n+1)]

temp=list(itertools.combinations(arr,m))

for i in temp:
  for k in i:
      print(k,end=' ')
  print()