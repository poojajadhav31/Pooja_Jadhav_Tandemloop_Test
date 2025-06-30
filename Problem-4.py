def count_multiples(lst):
    result = {}
    for i in range(1, 10):
        count = 0
        for num in lst:
            if num % i == 0:
                count += 1
        result[i] = count
    return result

# Example usage:
lst = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print("Output:", count_multiples(lst))
