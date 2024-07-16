MAX = 100
INF = int(1e9)

def floydWarshall(graph):
    V = len(graph)

    # Khởi tạo ma trận khoảng cách và ma trận đường đi
    dist = [[INF] * V for _ in range(V)]
    path = [[-1] * V for _ in range(V)]

    # Đường đi ngắn nhất từ một đỉnh đến chính nó là 0
    for i in range(V):
        dist[i][i] = 0

    # Khởi tạo ma trận khoảng cách với các trọng số của cạnh
    for u in range(V):
        for v in range(V):
            if graph[u][v] != 0:
                dist[u][v] = graph[u][v]
                path[u][v] = u  # Đường đi từ u đến v qua u

    # Áp dụng thuật toán Floyd-Warshall
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]

    # In ma trận khoảng cách cuối cùng
    print("Ma trận khoảng cách giữa các cặp đỉnh:")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("INF", end=" ")
            else:
                print(dist[i][j], end=" ")
        print()

    # In đường đi ngắn nhất giữa các cặp đỉnh
    print("\nĐường đi ngắn nhất giữa các cặp đỉnh:")
    for i in range(V):
        for j in range(V):
            if i != j and dist[i][j] != INF:
                print(f"Đường đi từ {i} đến {j}: ", end="")
                print_path(path, i, j)
                print(f" với chi phí {dist[i][j]}")

def print_path(path, i, j):
    if path[i][j] == -1:
        print("Không có đường đi", end="")
        return
    route = []
    while j != -1:
        route.append(j)
        j = path[i][j]
    print(" -> ".join(map(str, route[::-1])), end="")

# Ví dụ minh họa
graph = [
    [0, 3, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 7, 0, 2],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 3],
    [0, 0, 0, 0, 0, 0]
]

floydWarshall(graph)
