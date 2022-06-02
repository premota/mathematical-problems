# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

summation = 0
import math

for i in range(2, 2000000):
    
    #test_list helps create the if condition for selecting prime numbers
    test_list = []
    for j in range(2, int(math.sqrt(i) + 1)):
        if i%j == 0:
            test_list.append(i)
            break
    if test_list == []:
        summation += i
print(summation)
    