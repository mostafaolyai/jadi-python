def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        return f"Error: {e}."
    except ValueError as e:
        return f"Error: {e}."
    else:
        return result

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Result:", divide(num1, num2))
print("برنامه با موفقیت اجرا شد!")
