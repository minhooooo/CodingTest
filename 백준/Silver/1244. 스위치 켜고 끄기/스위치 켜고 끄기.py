import sys

n=int(input().strip())

switch=[0]

switch.extend(list(map(int,input().strip().split())))

case=int(input().strip())

for _ in range(case):
    a,b=map(int,input().strip().split())
    if a==1:
        flag=1
        while flag*b<=n:
            switch[flag*b]=(switch[flag*b]+1)%2
            flag+=1
    else:
        i=b-1
        j=b+1
        switch[b]=(switch[b]+1)%2
        while 1<=i<=n and 1<=j<=n:
            if switch[i]==switch[j]:
                switch[i]=(switch[i]+1)%2
                switch[j]=(switch[j]+1)%2
                i-=1
                j+=1
            else:
                break
for i in range(1,n+1):
    print(switch[i],end=' ')
    if i%20==0:
        print()