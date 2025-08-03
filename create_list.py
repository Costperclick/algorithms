import random


def create_randomised_list(desired_lenght):
    new_list = []
    for i in range(0, desired_lenght):
        new_list.append(i)
    random.shuffle(new_list)
    return new_list