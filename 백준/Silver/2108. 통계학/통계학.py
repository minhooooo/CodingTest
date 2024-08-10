import math
import sys
input=sys.stdin.readline
print=sys.stdout.write
temp=list()
count=int(input())
dics=dict()
sums=0
for _ in range(count):
    num=int(input())
    temp.append(num)
    dics.setdefault(num,0)
    dics[num]+=1
    sums+=num
temp.sort()
print(str(math.floor(sums/count+0.5))+'\n')
print(str(temp[int(count/2)])+'\n')
dics_keys=list(dics.keys())
dics_values=list(dics.values())
dics_reverse=dict()
for i in range(len(dics_values)):
    dics_reverse.setdefault(dics_values[i],[])
    dics_reverse[dics_values[i]].append(dics_keys[i])
dics_re_keys=sorted(dics_reverse.keys())
if len(dics_reverse[dics_re_keys[-1]])>1:
    dics_reverse[dics_re_keys[-1]].sort()
    print(str(dics_reverse[dics_re_keys[-1]][1])+'\n')
else:
    print(str(dics_reverse[dics_re_keys[-1]][0])+'\n')
print(str(temp[-1]-temp[0]))