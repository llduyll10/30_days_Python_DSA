def transform(expressions):
    s = []

    for symbol in expressions:
        if symbol.isalpha():
            print(symbol, end="")
        elif symbol == ')':
            print(s.pop(), end="")
        elif symbol != '(':
            s.append(symbol)
    print()

t = int(input())
for i in range(t):
    expressions = input()
    transform(expressions)
