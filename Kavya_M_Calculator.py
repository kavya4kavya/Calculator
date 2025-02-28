import math

while True:  # Main loop for the calculator
    #Giving the user options to choose from
    print("\n\n1.Decimal Operations\n2.Binary Operations\n3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 3:  
        break  # Exit the loop if choice is 3


    #Decimal Operations

    if choice==1:
        print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Floor Division\n6.Squareroot\n7.Cuberoot\n8.Exponent\n9.Factorial\n10.Modulo")
        choice=int(input("Enter your choice: "))
        
        if choice in[1,2,3,4,5,8,10]:#choices which need two operands
            operand_1=float(input("Enter first operand: "))
            operand_2=float(input("Enter second operand: "))                     
        
        match choice:
            case 1:
                solution=operand_1+operand_2
            case 2:
                solution=operand_1-operand_2
            case 3:
                solution=operand_1*operand_2
            case 4:
                if operand_2 == 0:
                    print("Division by zero not possible.")
                    continue
                else:
                    solution=operand_1/operand_2
            case 5:
                if operand_2 == 0:
                    print("Division by zero not possible.")
                    continue
                else:
                    solution=operand_1//operand_2
            case 6:
                operand_1=float(input("Enter the number: "))
                solution=math.sqrt(operand_1)            
            case 7:
                operand_1=float(input("Enter the number: "))
                solution=round(operand_1**(1/3),3)
            case 8:
                solution=operand_1**operand_2
            case 9:
                operand_1=float(input("Enter the number: "))
                solution=math.factorial(operand_1)
            case 10:
                solution=operand_1%operand_2
            case _:
                print("Invalid Choice")
                continue
        print("Soution: ",solution)


    #Binary Operations

    elif choice==2:
        print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
        choice=int(input("Enter your choice: "))
        
        if choice in[1,2,3,4]:#choices which need two operands
            bin1=input("Enter first binary number: ")
            bin2=input("Enter second binary number: ")
            dec1=int(bin1,2)
            dec2=int(bin2,2)
        
        match choice:
            case 1:
                solution=bin(dec1+dec2)[2:]
            case 2:
                solution=bin(dec1-dec2)[2:]
            case 3:
                solution=bin(dec1*dec2)[2:]
            case 4:
                if dec2==0:
                    print("Division by zero not possible.")
                    continue
                else:
                    solution=bin(int(dec1/dec2))[2:]
            case _:
                print("Invalid Choice")
                continue
        print("Solution: ",solution)
        
    else:
        print("Invalid Choice")
        continue
    
                      
                        
