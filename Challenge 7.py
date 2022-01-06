def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

primes = [] # list of primes
x = 10001 # go to the nth-number
n = 2 # start at number 2

while len(primes) != x+1:  # is n-th number on the list? +1 is because list is zero-based
    if is_prime(n):
        primes.append(n)  # add prime to the list
    n+=1 # increment n to check the next number

# print the last item in the list - the n-th number
print(primes[-1])
