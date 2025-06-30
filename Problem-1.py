class Calculator:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def operate(self, operation):
        if operation == 'add':
            return self.a + self.b
        elif operation == 'sub':
            return self.a - self.b
        elif operation == 'mul':
            return self.a * self.b
        elif operation == 'div':
            return self.a / self.b if self.b != 0 else "Division by zero error"
        else:
            return "Invalid Operation"

print("Simple Calculator")
a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
operation = input("Enter operation (add, sub, mul, div): ").strip().lower()

calc = Calculator(a, b)
result = calc.operate(operation)
print(f"Result: {result}")
