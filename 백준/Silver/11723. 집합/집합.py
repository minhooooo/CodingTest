import sys
input=sys.stdin.readline
print=sys.stdout.write
temp=set()
for _ in range(int(input())):
    ins=list(input().split())
    if ins[0]=="add":
        temp.add(ins[1])
    elif ins[0]=="remove":
        if ins[1] in temp:
            temp.remove(ins[1])
    elif ins[0]=="check":
        if ins[1] in temp:
            print("1\n")
        else:
            print("0\n")
    elif ins[0]=="toggle":
        if ins[1] in temp:
            temp.remove(ins[1])
        else:
            temp.add(ins[1])
    elif ins[0]=="all":
        temp=set({'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'})
    elif ins[0]=="empty":
        temp.clear()
