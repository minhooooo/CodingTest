import sys

input=sys.stdin.readline

score=0
total=0
for _ in range(20):
    a,b,c=input().strip().split()
    if c=="A+":
        score+=4.5*float(b)
        total+=float(b)
    elif c=="A0":
        score+=4.0*float(b)
        total+=float(b)
    elif c=="B+":
        score+=3.5*float(b)
        total+=float(b)
    elif c=="B0":
        score+=3.0*float(b)
        total+=float(b)
    elif c=="C+":
        score+=2.5*float(b)
        total+=float(b)
    elif c=="C0":
        score+=2.0*float(b)
        total+=float(b)
    elif c=="D+":
        score+=1.5*float(b)
        total+=float(b)
    elif c=="D0":
        score+=1.0*float(b)
        total+=float(b)
    elif c=="F":
        total+=float(b)
print(score/total)