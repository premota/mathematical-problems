# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 21000?

# n determines the number of times 2 multiplies itself
n = 1
product = 2

while n <= 999:
    product = product * 2
    n +=1
#convert every digit into a string to make it iterable
string = str(product)
summation = 0

for i in string:
    summation += int(i) 
print(summation)