# A command-line calculator.

# Function for addition
def addition():
    numbers = []

    while True:
        num = input("\nEnter a number to add (or 'done' to finish): ")

        if num.lower() == 'done':
            break

        # Convert the number into a float
        try:
            number = float(num)
            numbers.append(number)
        except ValueError:
            print("\nInvalid input. Please enter a number or 'done'.")

        if numbers:
            result = 0
            for num in numbers:
                result += num
            print(f"\nThe answer is {result}!")
        else:
            print("\nNo numbers to add.")

# Function for subtraction
def subtraction():
    numbers = []

    while True:
        num = input("\nEnter a number to subtract (or 'done' to finish): ")

        if num.lower() == 'done':
            break

        try:
            number = float(num)
            numbers.append(number)
        except ValueError:
            print("\nInvalid input. Please enter a number or 'done'.")

        if numbers:
            result = numbers[0]
            for num in numbers[1:]:
                result -= num
            print(f"\nThe answer is {result}!")
        else:
            print("\nNo numbers to subtract.")

# Function for multiplication
def multiplication():
    numbers = []

    while True:
        num = input("\nEnter a number to multiply (or 'done' to finish): ")

        if num.lower() == 'done':
            break

        try:
            number = float(num)
            numbers.append(number)
        except ValueError:
            print("\nInvalid input. Please enter a number or 'done'.")

        if numbers:
            result = 1
            for num in numbers:
                result *= num
            print(f"\nThe answer is {result}!")
        else:
            print("\nNo numbers to multiply.")

# Function for division
def division():
    numbers = []

    while True:
        num = input("\nEnter a number to divide (or 'done' to finish): ")

        try:
            number = float(num)
            numbers.append(number)
        except ValueError:
            print("\nInvalid input. Please enter a number or 'done'.")

        if num.lower() == 'done':
            break

        if numbers:
            result = numbers[0]
            for num in numbers[1:]:
                result /= num
            print(f"\nThe answer is {result}!")
        else:
            print("\nNo numbers to divide.")

# Main loop for user interaction
while True:
    prompt = "\nWhat would you like to do?"
    prompt += ("\n1. Addition"
               "\n2. Subtraction"
               "\n3. Multiplication"
               "\n4. Division"
               "\n5. Close program"
               "\nChoose an option (1-5): ")
    
    # Ask the user for their choice
    answer = input(prompt)

    # Run the function based on the user input
    if answer == '1':
        addition()
    elif answer == '2':
        subtraction()
    elif answer == '3':
        multiplication()
    elif answer == '4':
        division()
    elif answer == '5':
        break
