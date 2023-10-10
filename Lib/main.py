num1 = int(input("Enter the first value of the range: "))
num2 = int(input("Enter the second value of the range: "))

def summ(num1, num2):
    sum = 0
    for i in range(num1, num2+1):
        sum += i
    return sum

res = summ(num1, num2)
print("The sum of the range is: ", res)

