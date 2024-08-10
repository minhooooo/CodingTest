import math

while True:
    temp=input()
    if temp=='0':
        break
    temp=list(str(temp))
    start=1
    for i in range(0,math.floor(len(temp)/2)):
        if temp[i]!=temp[-1-i]:
            print("no")
            start=0
            break
    if start==1:
        print("yes")