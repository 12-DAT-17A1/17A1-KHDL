def is_perfect_number(num):
    if num <= 0:
        return False
    
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    
    return divisors_sum == num

# Nhập một số nguyên từ bàn phím
num = int(input("Nhập một số nguyên: "))

if is_perfect_number(num):
    print(num, "là một số hoàn hảo.")
else:
    print(num, "không phải là số hoàn hảo.")
