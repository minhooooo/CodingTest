import sys

input=sys.stdin.readline

n = int(input())
result = 0
bombo=[]
for _ in range(n):
    bombo.append(list(input())) 

def check():
    global result
    for i in range(n): 
        cnt = 1
        for j in range(n - 1):
            if bombo[i][j] == bombo[i][j + 1]:
                cnt += 1
                result = max(result, cnt)
            else:
                cnt = 1

    for i in range(n): 
        cnt = 1
        for j in range(n - 1):
            if bombo[j][i] == bombo[j + 1][i]:
                cnt += 1
                result = max(result, cnt)
            else:
                cnt = 1

for i in range(n):
    for j in range(n - 1):
            bombo[i][j], bombo[i][j + 1] = bombo[i][j + 1], bombo[i][j] 
            check()
            bombo[i][j + 1], bombo[i][j] = bombo[i][j], bombo[i][j + 1] 
        
            bombo[j][i], bombo[j + 1][i] = bombo[j + 1][i], bombo[j][i] 
            check()
            bombo[j + 1][i], bombo[j][i] = bombo[j][i], bombo[j + 1][i]
print(result)