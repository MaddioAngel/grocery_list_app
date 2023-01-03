import os
import subprocess
import json
import datetime
import settings
import random

days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def get_breakfast(num):
    data = ""
    with open('grocery_list_app/recipes/breakfast/breakfast.json') as file_:
        data = json.load(file_)[str(num)]
    return data

def get_lunch(num):
    data = ""
    with open('grocery_list_app/recipes/lunch/lunch.json') as file_:
        data = json.load(file_)[str(num)]
    return data

def get_dinner(num):
    data = ""
    with open('grocery_list_app/recipes/dinner/dinner.json') as file_:
        data = json.load(file_)[str(num)]
    return data

def get_snacks(num):
    return num

if __name__ == "__main__":
    print("Welcome to grocery list generator")
    print("In this program you can generate the meals for the week and their recipes")
    print("Then email you the list of ingredients you will need")
    print("and the ammount of money you will need")
    print("generating...")
    print()
    numbers_4_generation = [ random.sample(range(1,9), 7) , random.sample(range(1,8), 7), random.sample(range(1,10), 7) ]
    ingredients = {"breakfast":[], "lunch":[], "dinner":[]}
    for i in range(0,7):
        print("{}: ".format(days_of_the_week[i].upper()))
        breakfast = get_breakfast(numbers_4_generation[0][i])
        lunch = get_lunch(numbers_4_generation[1][i])
        dinner = get_dinner(numbers_4_generation[2][i])
        print("BREAKFAST: {}".format(breakfast["name"]))
        ingredients["breakfast"].append(breakfast["ingredients"])
        print("LUNCH: {}".format(lunch["name"]))
        ingredients["lunch"].append(lunch["ingredients"])
        print("DINNER: {}".format(dinner["name"]))
        ingredients["dinner"].append(dinner["ingredients"])
        print()
    for topic, items in ingredients.items():
        print(topic,"\n")
        for num, i in enumerate(items):
            print(num+1,"------------", i, end= "\n")
        print()
        




