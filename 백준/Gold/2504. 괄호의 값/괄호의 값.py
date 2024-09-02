import sys
input=sys.stdin.readline

arr=list(input().strip())

temp=[]
lenth=0

for i in arr:
    flag=0
    if i=='[' or i=='(':
        temp.append(i)
        lenth+=1
    elif (i==']' or i==')') and lenth>0:
        check=temp.pop()
        while check!='[' and check!='(':
            flag+=check
            check=temp.pop()
        if check=='[':
            if i==')':
                print("0")
                quit()
            if flag==0:
                temp.append(3)
            else:
                temp.append(3*flag)
        elif check=='(':
            if i==']':
                print("0")
                quit()
            if flag==0:
                temp.append(2)
            else:
                temp.append(2*flag)
        lenth-=1
    else:
        print("0")
        quit()

if lenth>0:
    print("0")
    quit()
else: print(sum(temp))
    