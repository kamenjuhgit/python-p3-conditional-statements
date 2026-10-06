def admin_login(username, password):
    # your code here
    try:
        if username.lower() == 'admin' and password == '12345':
            print("Access granted")
            return "Access granted"
        else:
            print("Access denied")
            return "Access denied"
    except TypeError:
        print("Arguements must be a string")

admin_login("admin", "12345")
admin_login("admin", "1235")
admin_login("ADmIN", "12345")



def hows_the_weather(temperature):
    # your code here
    try:
        if temperature < 40:
            print("It's brisk out there!")
            return "It's brisk out there!"
        elif temperature <= 65:
            print("It's a little chilly out there!")
            return "It's a little chilly out there!"
        elif temperature > 85:
            print("It's too dang hot out there!")
            return "It's too dang hot out there!"
        else:
            print("It's perfect out there!")
            return "It's perfect out there!"
    except TypeError:
        print("Must be int or float")
        return "Must be int or float"

hows_the_weather(30)
hows_the_weather(40)
hows_the_weather(85)
hows_the_weather(95)
hows_the_weather("hot")

def fizzbuzz(num):
    try:
        if num % 3 == 0:
            print("Fizz")
            return "Fizz"
        elif num % 5 == 0:
            print("Buzz")
            return "Buzz"
        elif num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
            return "FizzBuzz"
        else:
            print(num)
            return num
    except TypeError:
        print("Must be int or float")
        return "Must be int or float"

fizzbuzz(3)
fizzbuzz(5)
fizzbuzz(15)
fizzbuzz(7)
fizzbuzz("fifteen")

def calculator(operator, num1, num2):
    try:
        if operator == "+":
            num3 = num1 + num2
            print(num3)
            return num3
        elif operator == "-":
            num3 = num1 - num2
            print(num3)
            return num3
        elif operator == "*":
            num3 = num1 * num2
            print(num3)
            return num3
        elif operator == "/":
            num3 = num1 / num2
            print(num3)
            return num3
        else:
            print('Invalid Operation')
            return None
    except TypeError:
        print("Must be int or float")
        return "Must be int or float"

calculator("+",2,1)
calculator("-",84,72)
calculator("*",2,8)
calculator("/",2,7)
calculator("x",2,7)









