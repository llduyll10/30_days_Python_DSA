

def checkJacket(n,v):
    if n == 1:
        if v[0] == 1:
            return True
        else:
            return False

    count = 0
    for i in range(n):
        if v[i] == 0:
            count += 1

    if count == 1:
        return True
    else:
        return False

n = int(input())
v = list(map(int, input().split()))

if checkJacket(n,v):
    print("Yes")
else:
    print("No")