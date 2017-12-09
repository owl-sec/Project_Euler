prime = True
prime_sum = 0
prime_counter = 0
for num in range(int(200000000)):
    prime = True
    for i in range(2, num):
        if num%i ==0:
            j=num/i
            #print('%d equals %d * %d' % (num,i,j))
            prime = False
            break
        else:
            prime = True
    if prime == True:
        prime_counter = prime_counter + 1
        prime_sum = prime_sum + num
        print(num, "Prime Number","||", prime_counter, "Current Prime", "||", prime_sum, "Current Sum")
    if num == 200000000:
        print(prime_sum, "These are the droids you are looking for")         
        break
