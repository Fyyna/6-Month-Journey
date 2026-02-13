#this script helps 2 uncertain idiots to pick somewhere to go and eat
import random




def random_choice():

    choice = input("Input your choices seperated by space: ")
    choices = choice.split()
    text = random.choice(choices)
    return text


print(random_choice())