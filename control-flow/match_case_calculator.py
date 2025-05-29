num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /):")

match (operation):
    case "+":
        result  = num1+num2
        print(f"The result is: {result}")

    case "-":
        result = num2-num1
        print(f"The result is: {result}")
    
    case "*":
        result = num1*num2
        print(f"The result is: {result}")
    
    case "/":
        if num1 == 0:
            print("You can't divide by 0.")
        else:
            result = num2/num1
            print(f"The resut is: {result}")
    
