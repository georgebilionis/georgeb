def decodeNumbers(n):
    last_digit = n % 10  
    remaining_number = n // 10 
    num_digits = len(str(n)) 
    result = last_digit * (10 ** (num_digits - 1)) + remaining_number  
    return result


n = 12345
print(decodeNumbers(n))  