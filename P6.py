sumString = "1**2"
squareString = "(1"
for i in range(3,101):
    sumString = sumString + ' + ' + str(i) + '**2'
for i in range(3,101):
    squareString = squareString + ' + ' + str(i)

squareString = squareString + ') ** 2'
print(sumString)
print(eval(sumString))

print(squareString)
print(eval(squareString))

print(eval(squareString) - eval(sumString))
