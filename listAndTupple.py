def calculator():
    print("Advanced Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (**)")
    print("6. Square Root")
    print("7. Modulus (%)")
    
    while True:
        try:
            choice = int(input("\nEnter operation number (1-7) or 0 to exit: "))
            
            if choice == 0:
                print("Exiting calculator...")
                break
                
            if choice not in range(1,8):
                print("Invalid choice! Please select 1-7")
                continue
                
            if choice == 6:
                num = float(input("Enter number: "))
                result = num ** 0.5
                print(f"Square root of {num} = {result}")
                continue
                
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == 1:
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            elif choice == 2:
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            elif choice == 3:
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
            elif choice == 4:
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                else:
                    result = num1 / num2
                    print(f"{num1} / {num2} = {result}")
            elif choice == 5:
                result = num1 ** num2
                print(f"{num1} ** {num2} = {result}")
            elif choice == 7:
                result = num1 % num2
                print(f"{num1} % {num2} = {result}")
                
        except ValueError:
            print("Invalid input! Please enter numbers only.")
        except Exception as e:
            print(f"An error occurred: {e}")
            
if __name__ == "__main__":
    calculator()

    
