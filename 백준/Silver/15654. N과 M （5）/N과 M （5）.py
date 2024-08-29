import itertools

n,m=map(int,input().strip().split())

arr=sorted(map(int,input().strip().split()))

temp=list(itertools.permutations(arr,m))

for i in temp:
  for k in i:
      print(k,end=' ')
  print()

