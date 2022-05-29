def create_list(a):
    a = str(a)
    xyz = []
    for i in a:
        i = int(i)
        xyz.append(i)
    return xyz        
for i in range(900009,998001):
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