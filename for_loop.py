import random

count_6 = 0
count_1 = 0
two_6 = 0

previous = 0

for i in range(20):

    roll = random.randint(1, 6)

    print("Roll:", roll)

    if roll == 6:
        count_6 += 1

    if roll == 1:
        count_1 += 1

    if previous == 6 and roll == 6:
        two_6 += 1

    previous = roll

print("Number of 6s =", count_6)

print("Number of 1s =", count_1)

print("Two 6s in a row =", two_6)

# Question 2

# Question 2

total_jumping_jacks = 100
completed = 0

for i in range(1, 11):

    completed = completed + 10

    print("You completed", completed, "jumping jacks")

    if completed == 100:
        print("Congratulations! You completed the workout")
        break

    answer = input("Are you tired? ")

    if answer == "yes" or answer == "y":

        print("You completed a total of", completed, "jumping jacks")
        break

    elif answer == "no" or answer == "n":

        remaining = total_jumping_jacks - completed

        print(remaining, "jumping jacks remaining")