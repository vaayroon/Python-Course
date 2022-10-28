import logging
import traceback
import math


def add(num1, num2):
    return num1+num2


def sub(num1, num2):
    return num1-num2


def multi(num1, num2):
    return num1*num2


def div(num1, num2):
    return num1/num2


try:
    standard_input = 1, 2, '3', 4, 2, 15, -4  #standard inputs to AREPL vscode extension
    op1 = (int(input("Introduce the first operator --> ")))
    op2 = (int(input("Introduce the second operator --> ")))
    operator = input("Introduce the operation's number (addition: 1, subtraction: 2, multiplication: 3, division: 4) --> ")

    if operator == "1":
        print(add(op1, op2))
    elif operator == "2":
        print(sub(op1, op2))
    elif operator == "3":
        print(multi(op1, op2))
    elif operator == "4":
        print(div(op1, op2))
    else:
        print("Operation still not supported")
except Exception as e:
    print("An exception occurred: ", e)
    logging.error(traceback.format_exc())

print("Successfully executed operation")


'''
Exceptions lesson 2
'''


def divide():
    try:
        ope1 = (int(input("Introduce the first operator --> ")))
        ope2 = (int(input("Introduce the second operator --> ")))
        print("The result of the division is: " + str(ope1/ope2))
    except ValueError:
        print("The introduced value is not allowed")
    except Exception as e:
        print("An unexpected exception occurred: ", e)
    finally:
        print("Just a print test, to test 'Finally'")
        # Finally is so useful when we are working with database.
        # Because we always want to close the connection no matter what happens
    print("Successfully executed operation")


divide()


'''
Exceptions lesson 3
Instruction Raise
Own exceptions (with classes)
'''


def evaluate_age(age):
    if age < 0:
        raise ValueError("No negative ages allowed")
        # raise MiOwnError("No negative ages allowed")
        # We can create a class with the error type so the program can recognize the exception
    elif age < 20:
        return "You are very young"
    elif age < 40:
        return "Your are young"
    elif age < 65:
        return "You are not young anymore"
    elif age < 100:
        return "Take care of yourself ..."

eva1 = (int(input("Introduce your age: ")))
print(evaluate_age(eva1))

print("Ojo piojo")

'''-------------------------------------------'''


def calculatesqrt(num1):
    if num1 < 0:
        raise ValueError("The number cannot be negative")
    else:
        return math.sqrt(num1)


sop1 = (int(input("Introduce a number: ")))

try:
    print(calculatesqrt(sop1))
except ValueError as ve:
    print(ve)


print("Program completed")
