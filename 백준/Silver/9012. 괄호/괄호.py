def test():
    temp=list(input())
    count=0
    for i in temp:
        if i=='(':
            count+=1
        elif i==')':
            count-=1
            if count<0:
                return "NO"
    if count==0:
        return"YES"
    else: return "NO"
        
for _ in range(int(input())):
    print(test())