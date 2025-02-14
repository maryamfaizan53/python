# # #Question 1
# user_input1 = int(input("Enter first number: "))
# user_input2 = int(input("Enter second number: "))
# print(f'Here is the total um of your numbsers : {user_input1 + user_input2}')


 #Question 2
# def main():
#     user_input_animal: str = input("Enter your fav animal name: ")
#     print(f'My fav animal is also {user_input_animal}!')
# if __name__ == '__main__':
#     main()

#question 3
# from typing import Union

# def main():
#     degree: Union[float, str, int] = float(input("Enter temperature in Fahrenheit: "))
#     outcome = (degree - 32) * 5.0 / 9.0
#     print(f'Temperature: {degree}F = {outcome}C')

# if __name__ == '__main__':
#     main()

#question 4
# def main():
#     anton : int = 21
#     beth : int = 6 + anton
#     chen : int = 20 + beth
#     drew : int =  anton + chen
#     ethan : int = 20 + beth

 
#     print(f'Anton is {anton} years old')
#     print(f'Anton is {beth} years old')
#     print(f'Anton is {chen} years old')
#     print(f'Anton is {drew} years old')
#     print(f'Anton is {ethan} years old')
 
# if __name__ == '__main__':
#      main()

#Question 5
# def main():
#     user_input1 : int = float(input("Enter the lenght of triangle side 1 : "))
#     user_input2 : int = float(input("Enter the lenght of triangle side 2 : "))
#     user_input3 : int = float(input("Enter the lenght of triangle side 3 : "))
#     outcome = user_input1+user_input2+user_input3
#     print(f'The peremeter of Triangle is ({outcome})')
# if __name__ == '__main__':
#       main()

#question 6
def main():
 user_input: int = int(input("Ënter a number 2 square : "))
 outcome : int = user_input**2
 print(f'The square of {user_input} = {outcome}')
if __name__ == '__main__':
       main()
