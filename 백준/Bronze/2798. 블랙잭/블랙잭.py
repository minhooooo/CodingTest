import itertools

temp_input=list(map(int,input().split()))
temp_num=list(map(int,input().split()))
possible=itertools.combinations(temp_num,3)
mins=temp_input[1]
sums=temp_input[1]
for i in possible:
    if temp_input[1]-sum(i) <mins and sum(i)<=temp_input[1]:
        mins=temp_input[1]-sum(i)
        sums=sum(i)
print(sums)