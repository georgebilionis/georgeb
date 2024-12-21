def digital_root(num):
    total = 0
    while num > 0:
        total += num % 10 
        num //= 10 
    return total


num = 2468
print(digital_root(num))  