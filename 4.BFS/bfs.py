from queue import Queue

MAX = 100
V = None
E = None

visited = [False for i in range(MAX)]
path = [0 for i in range(MAX)]
graph = [[] for i in range(MAX)]

def bfs(s):
    for i in range(V): # Duyệt qua tất cả các đỉnh trong đồ thị
        visited[i] = False  # Đánh dấu tất cả các đỉnh là chưa được thăm
        path[i] = -1 # Khởi tạo đường đi với giá trị -1 cho tất cả các đỉnh

    q = Queue() # Tạo một hàng đợi để quản lý các đỉnh sẽ được thăm
    visited[s] = True  # Đánh dấu đỉnh bắt đầu là đã được thăm
    q.put(s)  # Thêm đỉnh bắt đầu vào hàng đợi

    while not q.empty(): # Lặp khi hàng đợi không rỗng
        u = q.get()

        for v in graph[u]:  # Duyệt qua tất cả các đỉnh kề của đỉnh u
            if not visited[v]:  # Nếu đỉnh v chưa được thăm
                visited[v] = True   # Đánh dấu đỉnh v là đã được thăm
                path[v] = u # Lưu đường đi từ đỉnh u đến đỉnh v
                q.put(v) # Thêm đỉnh v vào hàng đợi

def printPath(s, f):
    b = []  # Tạo danh sách để lưu đường đi
    if s == f:  # Nếu đỉnh bắt đầu và đỉnh kết thúc là cùng một đỉnh
        print(s)  # In đỉnh bắt đầu
        return
    if path[f] == -1:  # Nếu không có đường đi từ s đến f
        print("No path")  # In thông báo không có đường đi
        return

    while True:
        b.append(f) # Thêm đỉnh f vào danh sách
        f = path[f]  # Cập nhật f bằng đỉnh trước đó trên đường đi

        if f == s:  # Nếu f là đỉnh bắt đầu
            b.append(s) # Thêm đỉnh bắt đầu vào danh sách
            break   # Thoát khỏi vòng lặp


    for i in range(len(b)-1, -1,-1): # Duyệt ngược qua danh sách
        print(b[i], end="->")  # In từng đỉnh trong danh sách từ cuối đến đầu với dấu "->" sau mỗi đỉnh

if __name__ == "__main__":
    V, E = map(int, input().split())
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    s = 0
    f = 5
    bfs(s)
    printPath(s, f)