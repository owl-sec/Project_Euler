def main():
    n = int(600851475143)
    is_prime(n)

def is_prime(a):
    return all(a % i for i in xrange(2, a))

    if x:
        print("prime", is_prime(n))
    else:
        print("not prime")
