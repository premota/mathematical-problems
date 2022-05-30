#brings out prime factors for extremely large numbers e.g 600851475143

num = int(input('enter an integer\n>>'))
def find_primefactor(num):
    prime_factors = []

#half of the number is divided into smaller range. increasing computational speed within the range

    x = num
    a = x/65536
    q = int(a)
    while a <= x/2:
        e = 2
        for i in range(e, q):
            while x%i == 0:
                prime_factors.append(i)
                x = x/i
        e=q
        a += x/65536
    
    if len(prime_factors) == 0:      
        print(num)
    else:
        print(prime_factors)
find_primefactor(num)