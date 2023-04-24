import math
import numpy
import pandas as pd
import matplotlib.pyplot as plt

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
print(u[50])
print(u[51])
print(u[52])

# for i in range(100):
#     print("Randon Number " + str(i+1) + ": " + str(u[i]))

sample = []
sample_size = 110
sizes_of_each_sample = [10, 30, 50, 100, 250, 500, 1000]
expected_value = (1/(1/57))*(math.sqrt(math.pi / 2))
print(expected_value)
df = pd.DataFrame({'Sample Size': pd.Series(dtype='float'),
                   'Average Values': pd.Series(dtype='float')})

print(len(sizes_of_each_sample))
for i in range(len(sizes_of_each_sample)):
    sample.append([])
    current_sample_size = sizes_of_each_sample[i]
    curr_sample = sample[i]
    for j in range(sample_size):
        current_sample = 0
        for k in range(current_sample_size):
            random_number = u.pop(0)
            random_variable_value = math.sqrt(-6498 * math.log(1-random_number))
            current_sample += random_variable_value
        sample[i].append(current_sample/current_sample_size)
        df.loc[len(df.index)] = [sizes_of_each_sample[i], curr_sample[j]]

print(df)

"""
for value in sample:
    for avg in value:
        print(avg)
    print()
"""


#set columns to x and y axis
x = df['Sample Size']
y = df['Average Values']

plt.scatter(x, y)
plt.axhline(expected_value, label="Expected Value ($\mu_{x}$)")
plt.title('Law of Large Numbers', fontsize=18)
plt.xlabel('Sample Size (n)', fontsize=14)
plt.ylabel('Sample Mean ($m_{n}$)', fontsize=14)
plt.legend(("$m_{n}$", "Expected Value ($\mu_{x}$)"))
plt.savefig("graph.png")

