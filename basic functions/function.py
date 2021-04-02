def calculator():
    print("Enter a number")
    number = input()
    print("Enter another number")
    number2 = input()
    soma = str(number + number2)
    div = str(number / number2)
    mult = str(number * number2)
    menos = str(number - number2)
    print("Sum is: " + soma)
    print("Subtraction is: " + menos)
    print("Multiplication is: " + mult)
    print("Division is: " + div)

def timer():
    from datetime import datetime

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =" + current_time)

def today():
    from datetime import datetime
    today = datetime.today()
    todaystring = str(today)
    print(todaystring)