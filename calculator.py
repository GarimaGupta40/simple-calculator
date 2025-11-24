def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        raise ValueError("Unsupported operator")

if __name__ == "__main__":
    print("Simple Calculator - v1")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+ or -): ")

    result = calculate(a, b, op)
    print("Result:", result)
