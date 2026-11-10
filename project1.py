def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero is not allowed")
    return a/b

def power(a, b):
    return a ** b

def modulus(a,b):
    if b == 0:
        raise ZeroDivisionError("Modulus by zero is not allowed")
    return(a % b)


while True:
    print("\n====Menu Driven Calculator====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice(1-7):"))

        if choice==7:
            print("Thanku for using the calculator.Exiting...")
            break

        if choice <1 or choice >7:
            print("Invalid choice.Select 1 to 7.")
            continue

        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        if choice == 1:
            result = add(a, b)
            symbol = "+"

        elif choice  == 2:
            result = subtract(a, b)
            symbol = "-"

        elif choice == 3:
            result = multiply(a, b)
            symbol = "*"

        elif choice == 4:
            result = divide(a, b)
            symbol = "/" 

        elif choice == 5:
            result = power(a, b)
            symbol = "^"

        elif choice == 6:
            result = modulus(a, b)
            symbol = "%" 

        print(f"Result: {a:g} {symbol} {b:g} = {result:.2f}")

    except ZeroDivisionError as error :
        print("Error:", error)

    except  ValueError:
        print("Invalid input.Enter numbers only.")

    except  OverflowError:
        print("Error: Result is too large.")
