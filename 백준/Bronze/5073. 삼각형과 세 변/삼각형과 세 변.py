while(1):
    temp=sorted(list(map(int,input().strip().split())))
    if 0 in temp:
        exit()
    if temp[2]>=temp[1]+temp[0]:
        print("Invalid")
        continue
    lenth=len(set(temp))
    if lenth==1:
        print("Equilateral")
    elif lenth==2:
        print("Isosceles")
    else : 
        print("Scalene")
        