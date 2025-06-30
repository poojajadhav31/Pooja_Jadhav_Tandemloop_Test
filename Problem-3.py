def generate_series_2(a):
    count = a 
    if a % 2 != 0: 
        count = a - 1
    series = list(range(1, count + 1, 2))
    return series

# User interaction
a = int(input("Enter a number: "))
print("Output:", generate_series_2(a))
