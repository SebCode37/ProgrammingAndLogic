# CP1401 2021-1 Assignment 1
# Program 1 – SleepDebtCalc
# Student Name: Sebastian Wunderlich
# Date started: 24.11.2021

# 3. Sleep Debt Calculator: Repetition structures

# used while to check if number is in range and make sure its correct


# TOTAL_NIGHTS = 5
# SLEEP_TARGET = 8
# #constants
# print("This is the Sleep Calculator")
#
# night_count = 1
# total_actual = 0
# for sleep_actual in range(TOTAL_NIGHTS):
#     sleep_actual = float(input(f"Night {night_count} hours sleep: "))
#
#     while sleep_actual <0 or sleep_actual >24:
#         print("invalid numbers ")
#         sleep_actual = float(input(f"Night {night_count} hours sleep: "))
#     night_count += 1
#     total_actual += sleep_actual
#
# total_target = TOTAL_NIGHTS * SLEEP_TARGET
# sleep_debt = total_target - total_actual
# print("your sleep debt is: " + str(sleep_debt))