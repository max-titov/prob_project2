import math
from RandomNumberGenerator import *
from statistics import *

simulation_count = 500
max_call_attempts = 4
rand_values = generate_random_numbers(3000)
total_times = []

for i in range(simulation_count):
    call_attempts = 0
    time_spent = 0
    while call_attempts < max_call_attempts:  # CHANGE TO max_call_attempts
        randvar = rand_values.pop(0)
        time_spent += 6  # time to dial
        if randvar <= 1 and randvar > 0.5:
            # available
            randvar_exp_dist = rand_values.pop(0)  # reuse same rand var but scaled to 0-1
            # calcuate time to pick up using exponential distribution
            time_to_pick_up = -12*math.log(1-randvar_exp_dist)
            if time_to_pick_up <= 25:
                # customer picked up
                time_spent += time_to_pick_up
                break  # break out of while loop
            else:
                time_spent += 26  # time to ring through
        elif randvar < 0.2:
            # busy
            time_spent += 4  # time to detect busy signal
        else:
            #not there
            time_spent += 26  # time to ring through
        call_attempts += 1

    total_times.append(time_spent)

total_times.sort()

for time in total_times:
    print(time)

print("Mean:", mean(total_times))
print("Median:", median(total_times))
