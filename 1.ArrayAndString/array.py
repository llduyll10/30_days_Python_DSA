l = [1,2,3,4]
l.append(5)
l.insert(2,6)

n = len(l)
print(n)

result = l[2]
print(result)

l.pop()
print(l)

l.pop(2)
print(l)

l.clear()
print(l)

l.extend([5,6,7,8])
print(l)

l = l[0:2]
print(l)

for i in range(len(l)):
    print(l[i], end=", ")

for i in range(len(l)-1, -1, -1):
    print(l[i], end=", ")

s = "123abc"
if ord(s[0]) >=48 and ord(s[0]) <=57:
    print("digit")

s ="Learning Python"
result = s[1].isalpha()
print(result)

s="12"
number = int(s)
print(number)

numberT = 12345
s = str(numberT)
print(s)

s="algorithm"
c = s[2].upper()
print(c)