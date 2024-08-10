n=int(input())
n_list=list(map(int,input().split()))
n_dic=dict()
for i in n_list:
    n_dic.setdefault(i,1)
m=int(input())
m_list=list(map(int,input().split()))
for i in m_list:
    n_dic.setdefault(i,0)
    print(n_dic[i])