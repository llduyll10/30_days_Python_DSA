def binarySearch(arr, x):
    left = 0
    right = len(arr) - 1
     # Lặp lại cho đến khi chỉ số đầu vượt qua chỉ số cuối
    while left <= right:
        # Tìm chỉ số giữa
        mid = (left + right) // 2
        # Nếu phần tử giữa bằng x, trả về chỉ số giữa
        if arr[mid] == x:
            return mid
        # Nếu phần tử giữa lớn hơn x, tìm trong nửa bên trái
        elif arr[mid] > x:
            right = mid - 1
        # Nếu phần tử giữa nhỏ hơn x, tìm trong nửa bên phải
        else:
            left = mid + 1
    # Nếu không tìm thấy x, trả về -1
    return -1
arr = [2, 3, 4, 10, 40]
x = 10

result = binarySearch(arr, x)
print(result)