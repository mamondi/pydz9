num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))


def find_max(num1, num2, num3, num4):
    max_num = max(num1, num2, num3, num4)
    return max_num

res = find_max(num1, num2, num3, num4)

print("The maximum number is: ", res)