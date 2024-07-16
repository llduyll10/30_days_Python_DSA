MAX = 105
INF = 10**9

dist = [INF for _ in range(MAX)]
path = [-1 for _ in range(MAX)]
graph = []

def bellmanFord(graph, s):
    dist[s] = 0
    vertices = set()

    for u,v,_ in graph:
        vertices.add(u)
        vertices.add(v)
    V = len(vertices)

    for _ in range(V-1):
        for u,v,w in graph:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                path[v] = u

    # Kiểm tra chu trình trọng số âm
    for u,v,w in graph:
        if (dist[u] != INF) and (dist[u] + w < dist[v]):
            print("Đồ thị chứa chu trình trọng số âm")
            return

    # In ra chi phí
    for i in range(V):
        print(f"Đỉnh i={i}: chi phí={dist[i]}")


graph = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3)
]

src = 0  # Đỉnh nguồn

bellmanFord(graph, src)