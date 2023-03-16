x = 1000
a = 24693
c = 3517
K = 2**17

def printNum (x, n):
    x1 = (((a*x + c) % K))
    u1 = round(x1/K,4)
    
    print("Trial Number " + str(n) + ": " + str(u1))
    if n >= 53:
        return
    else:
        printNum(x1, n + 1)

printNum(1000, 1)



