dic={}
final=list()
for i in range(int(input())):
    word=input()
    dic.setdefault(len(word),[])
    dic[len(word)].append(word)
for i in sorted(list(dic.keys())):
    final.extend(sorted(set(dic[i])))
for i in final:
    print(i)