

def computePower(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result

x = 1
y = 7

print(computePower(x, y))
