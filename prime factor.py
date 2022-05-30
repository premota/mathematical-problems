#brings out all the prime factors of a number
#the largest possible prime factor of a number N cannot exceed N/2

prime_factors = []
x = int(input('enter an integer\n>>'))
b = x
a = round(x/2)
for i in range(2, a):
    if x/i ==1:
        prime_factors.append(i)
        x = x/i
    else:
        while x%i == 0:
            prime_factors.append(i)
            x = x/i
        
#if there's no prime factor, d number is a prime number

if len(prime_factors) == 0:      
    print(b)
else:
    print(prime_factors)