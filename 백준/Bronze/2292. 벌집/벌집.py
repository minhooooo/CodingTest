target=int(input())
count=1
while True:
    if target<=1:
        print(count)
        break
    target=target-(6*count)
    count=count+1
    