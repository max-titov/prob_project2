import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x = 1000
a = 24693
c = 3967
K = 2**18
u = []


def rand_num_generator(seed, a, c, k, n):
    # n is how many randon numbers will be created
    x = seed
    for i in range(n):
        x = (a * x + c) % k
        u.append(x / k)
    return u


# Used for determining randon numbers
u = rand_num_generator(x, a, c, K, 215000)
# print(u[50])
# print(u[51])
# print(u[52])

# for i in range(100):
#     print("Randon Number " + str(i+1) + ": " + str(u[i]))

sample = []
sample_size = 110
n = [3, 9, 27, 81]
K = [5, 25, 110, 550]

for i in range(4):
    sample.append([])
    current_sample_size = n[i]
    current_ind_estimates = K[i]
    for j in range(current_ind_estimates):
        current_sample = 0
        for k in range(current_sample_size):
            random_number = u.pop(0)
            random_variable_value = math.sqrt(
                (-2*math.log(1-random_number))/((1/(4*math.pi))**2))
            current_sample += random_variable_value
        sample[i].append(current_sample/current_sample_size)

means = []
vars = []
for i in range(4):
    mean = 0
    var = 0
    estimates = len(sample[i])
    for j in range(estimates):
        mean += sample[i][j]
        var += sample[i][j]**2
    mean = mean/estimates
    var = math.sqrt(var/estimates-mean**2)
    means.append(mean)
    vars.append(var)

zn = []
for i in range(4):
    zn.append([])
    estimates = len(sample[i])
    for j in range(estimates):
        zn[i].append((sample[i][j] - means[i])/vars[i])
    zn[i].sort()

fn = []
specific_x_vals = [-1.4, -1.0, -0.5, 0, 0.5, 1.0, 1.4]
for i in range(4):
    fn.append([])
    estimates = len(zn[i])
    for j in range(len(specific_x_vals)):
        x_val = specific_x_vals[j]
        k = 0
        for k in range(estimates):
            if x_val < zn[i][k]:
                break
        if k == 0:
            fn[i].append(0)
        else:
            fn[i].append(k/estimates)

mad = []
madx = []
mady = []
for i in range(4):
    max_abs_diff = 0
    max_abs_diff_x = 0
    max_abs_diff_y = 0
    print('\n i:', i)
    for j in range(len(specific_x_vals)):
        x_val = specific_x_vals[j]
        gaussian_val = norm.cdf(x_val)
        fn_val = fn[i][j]
        abs_diff = abs(fn_val-gaussian_val)
        print("%.4f" % abs_diff)
        if abs_diff > max_abs_diff:
            max_abs_diff = abs_diff
            max_abs_diff_x = x_val
            max_abs_diff_y = fn_val
    mad.append(max_abs_diff)
    madx.append(max_abs_diff_x)
    mady.append(max_abs_diff_y)

print('\n MAX VALUES')
for i in range(4):
    print("%.4f" % mad[i])

for i in range(4):
    # define x and y values to use for CDF
    standard_x = np.linspace(-2.5, 2.5, 1000)
    standard_y = norm.cdf(standard_x)

    # plot normal CDF
    plt.plot(standard_x, standard_y, label='Standard Normal CDF')
    empirical_x = []
    empirical_y = []
    for j in range(len(specific_x_vals)):
        x_val = specific_x_vals[j]
        fn_val = fn[i][j]
        empirical_x.append(x_val)
        empirical_y.append(fn_val)

    plt.plot(empirical_x, empirical_y, marker='o',
             color='g', label='Empirical CDF of Zn')
    # plot line between empirical and standard at Maximum Absolute Difference
    madx_values = [madx[i], madx[i]]
    mady_values = [mady[i], norm.cdf(madx[i])]
    plt.plot(madx_values, mady_values, 'r',
             label='Maximum Absolute Difference')
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Probability')
    plt.show()

print("done")
