l = [5,7,8,3,6]
l.sort(reverse=False)
print(l)

l.sort(reverse=True)
print(l)

v=[5,7,8,3,6]
v[1:4] = sorted(v[1:4])
print(v)