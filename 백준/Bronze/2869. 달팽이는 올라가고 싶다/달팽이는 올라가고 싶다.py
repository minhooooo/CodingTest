import math
a,b,v=map(int,input().split())
temp=v-b
print(math.ceil(temp/(a-b)))