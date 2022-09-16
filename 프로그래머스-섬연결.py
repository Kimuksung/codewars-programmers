# 프로그래머스-섬연결하기
def solution(n, costs):
    answer = 0
    costs=sorted(costs , key=lambda x:x[2])
    parent = [i for i in range(n)]
    def find(node):
        if parent[node]!=node:
            return find(parent[node])
        return node
    
    def union(A,B):
        A,B=find(A),find(B)
        if A==B:
            return False

        if A<B:
            parent[B]=A
        else:
            parent[A]=B
        return True
    
    for start,end,value in costs:
        if not union(start,end):
            continue
        answer+=value
    
    return answer