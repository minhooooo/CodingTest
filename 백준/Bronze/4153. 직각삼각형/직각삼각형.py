while True:
    temp=list(map(int,input().split()))
    temp.sort()
    if temp[0]==0:
        break
    if temp[0]**2+temp[1]**2==temp[2]**2:
        print("right")
    else:
        print("wrong")