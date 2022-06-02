# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


import math
prime_num = []
n = 0

#when number of prime numbers in the list reaches the target, iteration stops
while len(prime_num) <= 10001:
    for i in range(n, n+1):
        test_list = []
        #test_list helps create the if condition for selecting prime numbers
        
        for j in range(2, int(math.sqrt(i)+1)):
            if i%j == 0:
                test_list.append(i)
                break
        if len(test_list) == 0 and i !=1:
            prime_num.append(i)
    n += 1
#last prime number
print(prime_num[-1])

print(len(prime_num))
#considering 0-indexing, len(prime_num) = 10002, but total value in list = 1001