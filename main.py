from collections import deque
import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    edges = []
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        idx += 2
        edges.append((u, v))

    graph = [[] for _ in range(n)]
    indegree = [0] * n
    
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
    
    top_order = []
    
    while q:
        u = q.popleft()
        top_order.append(u)
        
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    if len(top_order) != n:
        print(-1)
    else:

        print(' '.join(str(x + 1) for x in top_order))

if __name__ == "__main__":
    main()
