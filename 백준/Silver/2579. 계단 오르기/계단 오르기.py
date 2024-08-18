import sys

input=sys.stdin.readline

count=int(input())
stair=[0]*301
score=[0]*301

for i in range(count):
    stair[i+1]=int(input())
score[1]=stair[1]
score[2]=stair[1]+stair[2]
score[3]=max(stair[1]+stair[3],stair[2]+stair[3])
for i in range(4,count+1):
    score[i]=max(score[i-2]+stair[i],score[i-3]+stair[i-1]+stair[i])
print(score[count])
