import math

x = 1000
a = 24693
c = 3517
K = 2**17

values = []

def NumGenerator (x, n):
    x1 = (((a*x + c) % K))
    u1 = round(x1/K,4)

    # print("Random Number " + str(n) + ": " + str(u1))
    values.append(u1)

    if n >= 53:
        return
    else:
        NumGenerator(x1, n + 1)

NumGenerator(1000, 1)


# Second Part

busy = 0.2
unavailable = 0.3
available = 0.5

for i in range(50):
    r = values[i]

    if r < busy:
        outcome = 'busy'
    elif r < busy + unavailable:
        outcome = 'unavailable'
    else:
        outcome = 'available'

    print(outcome)

# Third Part

def inverse_cdf(i):
    return -12 * math.log(1-i)

a = values[0]
time = inverse_cdf(a)
print(time)

















# def linear_congruential_generator(seed, a, c, k, n):
#     x = seed
#     u = []
#     for i in range(n):
#         x = (a * x + c) % k
#         u.append(x / k)
#     return u

# u = linear_congruential_generator(1000, 24693, 3517, 2**17, 53)
# print(u[50:53])