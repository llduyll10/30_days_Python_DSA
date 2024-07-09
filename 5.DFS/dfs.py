MAX = 100
E = None
V = None

visited = [False for _ in range(MAX)]
path = [0 for _ in range(MAX)]
graph = [[] for _ in range(MAX)]

def dfs(s):
    for i in range(V):
        visited[i] = False
        path[i] = -1
    stack = []

    visited[s] = True
    stack.append(s)

    while stack:
        u = stack.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                path[v] = u
                stack.append(v)
def printPath(s, f):
    b = []
    if s == f:
        print(s)
        return
    if path[f] == -1:
        print('no path')
        return
    while True:
        b.append(f)
        f = path[f]

        if f == s:
            b.append(s)
            break
    for i in range(len(b)-1, -1, -1):
        print(b[i], end='->')

if __name__ == "__main__":
    V, E = map(int, input().split())
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    s = 0
    dfs(s)
    printPath(s, 5)