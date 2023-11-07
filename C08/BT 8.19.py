def reverse_odd_sequence(n):
    odd_numbers = []

    for i in range(1, n * 2, 2):
        odd_numbers.append(i)

    odd_numbers.reverse()
    return odd_numbers

n = int(input("Nhập số lượng số lẻ: "))

result = reverse_odd_sequence(n)
print("Dãy số lẻ đảo ngược:", result)
