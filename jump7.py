def include7(n):
    if 0 == n%7:
        return 0
    elif n//10 == 7:
        return 0
    elif 7 == n%10:
        return 0
    else:
        return 1 
i = 1
while i<100:
    if (0 == include7(i)):
        i += 1
        continue
    else:
        print(i)
        i += 1
