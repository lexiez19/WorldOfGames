import random
import os
import time


def clear():
    time.sleep(0.7)
    os.system('cls')


def generate_sequence(dfc_generate_sequence):
    random_list = []
    for i in range(dfc_generate_sequence):
        n = random.randint(1, 102)
        random_list.append(n)
    print("Are you ready? in 1 Seconds I will show you the list")
    time.sleep(1)
    print("Remember this list of Numbers", random_list)
    clear()
    return random_list


def get_list_from_user(dfc_list_from_user):
    user_input_list = []
    for i in range(dfc_list_from_user):
        input_number = int(input("Enter a Number\n"))
        user_input_list.append(input_number)
    return user_input_list


def is_list_equal(ran_list, user_in_list):
    ran_list.sort()
    user_in_list.sort()
    if ran_list == user_in_list:
        return True
    else:
        return False


def MemoryGameplay(dfc):
    z = generate_sequence(dfc)
    y = get_list_from_user(dfc)
    is_equal = is_list_equal(z, y)
    return is_equal
