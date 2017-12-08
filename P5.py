haveFound = True
Number = 0
secondNumber = 0
notExiting = True
dividing = 10
while haveFound:
    Number = Number + 1
    secondNumber = 0
    while (secondNumber < (dividing + 1)):
        secondNumber = secondNumber + 1
        if (Number % secondNumber) != 0:
            secondNumber = 22
        elif (secondNumber > dividing):
            secondNumber = 22
        elif (((Number % dividing) == 0) & (secondNumber == dividing)):
            haveFound = False
print(Number)
