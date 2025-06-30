def generate_series_1(a):
    series = []
    for i in range(a):
        series.append(2*i + 1)
    return series

# Example usage:
a = int(input("Enter a number: "))
print("Output:", generate_series_1(a))
