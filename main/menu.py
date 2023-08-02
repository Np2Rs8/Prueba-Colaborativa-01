from os import system
import msvcrt
from calculator import (
    fun_add,
    fun_subtraction,
    fun_multiply,
    fun_divide,
    fun_allInOneEcuation
)


def fun_displayMenu():
    print("#=====# Welcome to our calculator #=====#")
    
    option = fun_menuMessage()
    
    while option != 6:
        match option:
            case 1:
                system("cls")
                print("#=====# Addition #=====#\n")
                values = fun_getNumbersValues()
                print(f"The result for the addition is: {fun_add(values[0], values[1])}")
            case 2:
                system("cls")
                print("#=====# Subtraction #=====#\n")
                values = fun_getNumbersValues()
                print(f"The result for the subtraction is: {fun_subtraction(values[0], values[1])}")
            case 3:
                system("cls")
                print("#=====# Multiplication #=====#\n")
                values = fun_getNumbersValues()
                print(f"The result for the multiplication is: {fun_multiply(values[0], values[1])}")
            case 4:
                system("cls")
                print("#=====# Division #=====#\n")
                values = fun_getNumbersValues()
                print(f"The result for the division is: {fun_divide(values[0], values[1])}")
            case 5:
                while True:                
                    system("cls")
                    print("#=====# All in one #=====#\n")
                    fun_showEcuationOperators()
                    
                    print("Type '0' to go back...")
                    
                    ecuation = input("Ecuation: ")
                    if(ecuation == "0"):
                        system("cls")
                        break
                    
                    formattedEquation = fun_fixEcuationFormat(ecuation)
                    
                    result = fun_allInOneEcuation(formattedEquation)
                    if(result == "ERROR"):
                        pass
                    else:
                        print(f"The result for the ecuation is: {result}")
                    
                    print("\nPress any key to continue...")
                    msvcrt.getch()
            case _:
                system("cls")
                print("That's an undefined option.")
        option = fun_menuMessage()
    
    system("cls")


def fun_menuMessage():
    print("\nPlease, select an option...")
    print("1. Addition.")
    print("2. Subtraction.")
    print("3. Multiplication.")
    print("4. Division.")
    print("5. All in one.")
    print("6. Exit.")
    
    try:
        return int(input(">>> "))
    except Exception as e:
        return("ERROR")

def fun_showEcuationOperators():
    
    operators = [
        {
            "operator": "Addition",
            "abbreviation": "+"
        },
        {
            "operator": "Subtraction",
            "abbreviation": "-"
        },
        {
            "operator": "Multiplication",
            "abbreviation": "*"
        },
        {
            "operator": "Division",
            "abbreviation": "/"
        },
        {
            "operator": "Power",
            "abbreviation": "**"
        },
        {
            "operator": "Square root",
            "abbreviation": "sqrt()"
        },
        {
            "operator": "Cube root",
            "abbreviation": "cbrt()"
        },
        {
            "operator": "Factorial",
            "abbreviation": "fact()"
        },
        {
            "operator": "New coming soon",
            "abbreviation": "..."
        }
    ]
    
    print("#=========================#===============#")
    print("‖ Operator name           # Abbreviation  ‖")
    print("#=========================#===============#")
    for op in operators:
        operator = op["operator"]
        abbreviation = op["abbreviation"]
        message = "‖ {:<24}‖{:>14} ‖".format(operator, abbreviation)
        print(message)
        print("#=========================#===============#")
    print()

def fun_fixEcuationFormat(ecuation):
    formattedEquation = ecuation.replace("sqrt", "math.sqrt")
    formattedEquation = formattedEquation.replace("cbrt", "math.cbrt")
    formattedEquation = formattedEquation.replace("fact", "math.factorial")
    return formattedEquation


def fun_getNumbersValues():
    num1 = int(input("Please write the first value: "))
    num2 = int(input("Please write the second value: "))
    
    return num1, num2
