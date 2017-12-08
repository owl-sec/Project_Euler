Sum = 0
current = 1
previous = 1
storage = 0
while (current < 4000000):
    storage = previous
    previous = current
    current = previous + storage
    print(Sum)
    if (current%2) == 0:
       Sum = Sum + current
