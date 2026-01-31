from decimal import Decimal, getcontext

getcontext().prec = 1000  # precision = 1000 digits

while True:
    print("\nHigh-Precision Calculator (type 'exit' to quit)")
    
    a = input("First number: ")
    if a.lower() == "exit":
        break

    op = input("Operation (+ - * /): ")
    b = input("Second number: ")

    a = Decimal(a)
    b = Decimal(b)

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        print("Result:", a / b)
    else:
        print("Invalid operation")
