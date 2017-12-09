600851475143
prime = True
for num in range(int(10), 2, -1):     #to iterate between 10 to 20
    prime = True
    for i in range(2,num):    #to iterate on the factors of the number
      if num%i == 0:         #to determine the first factor
         j=num/i             #to calculate the second factor
         print('%d equals %d * %d' % (num,i,j))
         prime = False
          #to move to the next number, the #first FOR
         break
      else:                  # else part of the loop
          prime = True
    if prime == True:
        print(num, ' is prime')
    if (600851475143 % num) == 0:
        print(num, ' GOTTAM')
        break
