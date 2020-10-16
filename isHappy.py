import sys as sys

# Function to add squares of individual digits of a number
def sumSquare(number):
    string = str(number)
    sum = int(0)
    for x in string:
        sum += (int(x))**2
    return sum


# Function to determine if number is happy
def isHappy(number):
    history = []
    num1 = int(0)
    while (num1 not in history):
        history.append(number)
        num1 = sumSquare(number)
        if num1 == 1:
            return True, history
        number = num1
        
    history.append(number)
    return False, history


if __name__ == "__main__":
    print("This program will determine if a number is \"Happy\"")
    # Get user input
    number = input("Enter an integer: ")
    try:
        number = int(number)
        if number < 0: # Fix negative sign
            number *= -1
    except ValueError:
        print("Please enter an integer")
        print("Program terminated")
        sys.exit()

    #Process input
    isItHappy, history = isHappy(number)

    # Output results
    if isItHappy:
        print("Number is happy")
    else:
        print("Number is not happy")
    print("Here is the number cycle:")
    print(history)
    print("Program ended normally")
    sys.exit()

    