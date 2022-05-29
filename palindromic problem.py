#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def create_list(a):
#function to convert integer values into list
    a = str(a)
    xyz = []
    for i in a:
        i = int(i)
        xyz.append(i)
    return xyz        
for i in range(900009,998001):
#iterating between the highest possible integer gotten by multiplying two 3_digit numbers and an arbitrary value.
#the range between these values must contain multiple palindromic numbers

    x = create_list(i)
    if x[0] == x[5] and x[1] == x[4] and x[2]== x[3]:
        b = ''
        for i in x:
            b += str(i)
        b = int(b)
        c = 999
        while b%c != 0 and c>=100:
            c = c-1
        if b/c < 1000:
            print(c,b)
