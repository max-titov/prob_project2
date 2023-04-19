import math
import numpy

x = 1000
a = 24693
c = 3967
K = 2**18
u = []

def rand_num_generator(seed, a, c, k, n):
    #n is how many randon numbers will be created
    x = seed
    for i in range(n):
        x = (a * x + c) % k
        u.append(x / k)
    return u


u = rand_num_generator(x,a,c,K,215000)  #Used for determining randon numbers
print(u[0])
print(u[1])
print(u[2])
print(u[50])
print(u[51])
print(u[52])

# for i in range(100):
#     print("Randon Number " + str(i+1) + ": " + str(u[i]))

sample = []
sample_size = 110
sizes_of_each_sample = [10, 30, 50, 100, 250, 500, 1000]

for i in range(len(sizes_of_each_sample)):
    sample.append([])
    current_sample_size = sizes_of_each_sample.pop(0)
    for j in range(sample_size):
        current_sample = 0
        for k in range(current_sample_size):
            random_number = u.pop(0)
            random_variable_value = math.sqrt((-2*math.log(1-random_number))/((1/(4*math.pi))**2))
            current_sample += random_variable_value
        sample[i].append(current_sample/current_sample_size)

for value in sample:
    for avg in value:
        print(avg)
    print()




