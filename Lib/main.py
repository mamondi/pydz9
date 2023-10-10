lenth = int(input("Enter the lenth of the line: "))
symbol = input("Enter the symbol: ")
direction = input("Enter the direction[1 - horizontal/2 - vertical]: ")

if direction == "1":
    for i in range(lenth):
        print(symbol, end="")
elif direction == "2":
    for i in range(lenth):
        print(symbol)
