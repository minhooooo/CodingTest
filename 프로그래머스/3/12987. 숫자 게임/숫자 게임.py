import itertools

def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    j=0
    for i in A:
        if i<B[j]:
            answer+=1
            j+=1
    return answer
    