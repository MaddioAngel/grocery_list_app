import os
import subprocess
import json
from turtle import clear
import settings
import random

days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def get_breakfast(num):
    return num

def get_lunch(num):
    return num

def get_dinner(num):
    return num

def get_snacks(num):
    return num

if __name__ == "__main__":
    print("Welcome to grocery list generator")
    print("In this program you can generate the meals for the week and their recipes")
    print("Then email you the list of ingredients you will need")
    print("and the ammount of money you will need")
    print("generating...")
    print()
    numbers_4_generation = [ random.sample(range(11), 7) , random.sample(range(11), 7), random.sample(range(11), 7) ]
    for i in range(0,7):
        print("{}: ".format(days_of_the_week[i].upper()))
        print("BREAKFAST: {}".format(get_breakfast(numbers_4_generation[0][i])))
        print("LUNCH: {}".format(get_lunch(numbers_4_generation[1][i])))
        print("DINNER: {}".format(get_dinner(numbers_4_generation[2][i])))
        print()


