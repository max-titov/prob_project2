# import numpy as np
# import scipy.stats as stats

# # Set up constants and variables
# num_sims = 500
# total_times = []

# # Define the random variable to determine customer availability
# customer_type = stats.rv_discrete(
#     values=(["busy", "unavailable", "available"], [0.2, 0.3, 0.5]))

# # Define the random variable to determine how long it takes for an available customer to answer the call
# X_mean = 12
# X = stats.expon(loc=0, scale=X_mean)

# # Perform the Monte Carlo simulation
# for i in range(num_sims):
#     attempts = 0
#     time_spent = 0
#     while attempts < 4:
#         # Determine customer availability
#         customer = customer_type.rvs()
#         if customer == "available":
#             # Determine time to answer call
#             answer_time = X.ppf(np.random.rand())
#             time_spent += 6 + max(answer_time, 25) + 1
#             if answer_time < 25:
#                 # Customer answers the call
#                 total_times.append(time_spent)
#                 break
#         else:
#             # Customer is busy or unavailable
#             time_spent += 6 + 25 + 1
#         attempts += 1
#     else:
#         # Customer does not answer after 4 attempts
#         total_times.append(time_spent)

# # Analyze the results
# mean_time = np.mean(total_times)
# std_time = np.std(total_times)
# max_time = np.max(total_times)

# print(f"Mean time spent trying to reach a customer: {mean_time:.2f} seconds")
# print(f"Standard deviation of time spent: {std_time:.2f} seconds")
# print(f"Maximum time spent: {max_time: .2f} seconds")


list = [1,2,3,4]
x = list.pop(0)
print(x)
print(list)

list2 = [1,3,5]
list2.reverse()
print(list2)