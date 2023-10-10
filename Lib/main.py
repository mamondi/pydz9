num1 = int(input("Enter six numbers, first number:  "))
num2 = int(input("Second number:  "))
num3 = int(input("Third number:  "))
num4 = int(input("Fourth number:  "))
num5 = int(input("Fifth number:  "))
num6 = int(input("Sixth number:  "))

def happynum(num1, num2, num3, num4, num5, num6):
    if num1 + num2 + num3 == num4 + num5 + num6:
        return num1 + num2 + num3 == num4 + num5 + num6

if happynum(num1, num2, num3, num4, num5, num6):
    print("It's a happy number!")
else:
    print("It's a nonhappy number :(")

