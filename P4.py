numberAsString = '0'
numberAsList = []
currentLargest = 0
for i in range(999,100, -1):
    for u in range(999,100, -1):
        numberAsString = str(i*u)
        numberAsList = list(numberAsString)
        if (len(numberAsList) == 5):
            if ((numberAsList[0] == numberAsList[4]) & (numberAsList[1] == numberAsList[3])):
                print(numberAsString, ' is a palindrome')
                if ((u*i) > currentLargest):
                    currentLargest = (u*i)
        else:
            if ((numberAsList[0] == numberAsList[5]) & (numberAsList[1] == numberAsList[4]) & (numberAsList[2] == numberAsList[3])):
                print(numberAsString, ' is a palindrome')
                if ((u*i) > currentLargest):
                    currentLargest = (u*i)

def printLargest():
    print(currentLargest)
