from calculator import (
    fun_add,
    fun_subtraction,
    fun_multiply,
    fun_divide
)


def fun_displayMenu():
    print("#=====# Welcome to our calculator #=====#")
    
    option = fun_menuMessage()
    
    while option != 5:
        match option:
            case 1:
                values = fun_getNumbersValues()
                print(f"The result for the addition is: {fun_add(values[0], values[1])}")
            case 2:
                values = fun_getNumbersValues()
                print(f"The result for the subtraction is: {fun_subtraction(values[0], values[1])}")
            case 3:
                values = fun_getNumbersValues()
                print(f"The result for the multiplication is: {fun_multiply(values[0], values[1])}")
            case 4:
                values = fun_getNumbersValues()
                print(f"The result for the division is: {fun_divide(values[0], values[1])}")
            case _:
                print("That's is an undefined option.")
            
        option = fun_menuMessage()
                
        
        
        
def fun_menuMessage():
    print("\nPlese, select an option...")
    print("1. Addition.")
    print("2. Subtraction.")
    print("3. Multiplication.")
    print("4. Division.")
    print("5. Exit.")
    
    return int(input(">>> "))


def fun_getNumbersValues():
    num1 = int(input("Please write the first value: "))
    num2 = int(input("Please write the second value: "))
    
    return num1, num2
    