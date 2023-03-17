x = 1000
a = 24693
c = 3517
K = 2**17

values = []


def NumGenerator(x, n, count):
    x1 = (((a*x + c) % K))
    u1 = round(x1/K, 4)

    #print("Random Number " + str(n) + ": " + str(u1))
    values.append(u1)

    if n >= count:
        return
    else:
        NumGenerator(x1, n + 1, count)


def rand_num_generator(seed, a, c, k, n):
    x = seed
    u = []
    for i in range(n):
        x = (a * x + c) % k
        u.append(x / k)
    return u

# u = linear_congruential_generator(1000, 24693, 3517, 2**17, 53)


def generate_random_numbers_recursive(count):
    global values
    values = []
    NumGenerator(1000, 1, count)
    return values


def generate_random_numbers(count):
    return rand_num_generator(x, a, c, K, count)

#NumGenerator(1000, 1)


# Second Part

# isAvailable = False
# isBusy = False
# isNotThere = False


# if values[0] < 0.5:
#     isAvailable = True
# elif values[0] < 0.7:
#     isBusy = True
# else:
#     isNotThere = True


# print(u[50:53])
