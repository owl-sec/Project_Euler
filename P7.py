prime = True
current_prime = 0
for num in range(int(2), (999999999)):
    prime = True
    for i in range(2,num):
      if num%i == 0:
         j=num/i
         prime = False
         break
      else:
          prime = True
    if prime == True:
        current_prime = current_prime + 1
        if current_prime == 10001:
            print(num, "These are the droids you are looking for")
        

   
