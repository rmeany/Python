# Simple Calculator based on user input

# Add both numbers
def add_numbers(num1, num2):
    return num1+num2

# Subtract second number from first number
def subtract_numbers(num1, num2):
    return num1-num2

# Multiply both numbers
def multiply_numbers(num1, num2):
    return num1*num2

# Divide the first number by the second number
def divide_numbers(num1, num2):
    return num1/num2


while True:
    choice = input("Please choose from one of the following:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n\n")
    if choice in ('1','2','3','4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(f"{num1} + {num2} = ", add_numbers(num1,num2))
        if choice == '2':
            print(f"{num1} - {num2} = ", subtract_numbers(num1,num2))
        if choice == '3':
            print(f"{num1} x {num2} = ", multiply_numbers(num1,num2))
        if choice == '4':
            print(f"{num1} / {num2} = ", divide_numbers(num1,num2))

        # check if user wants another calculation
        another = input("Let's do next calculation? (y/n): ")
        if another == "n":
          break
    else:
        print("Invalid option")
