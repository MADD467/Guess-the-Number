#from tkinter import *
import random

#fenetre = Tk()

#label = Label(fenetre, text="Guess the number the bomb will blow up")

choix = range(1, 10)
number = random.choice(choix)
#print(number)

chances = 3
print("Vous avez", chances, "chances ")

for i in range(3):
    user = input("Choisissez un nombre de 1 à 10: ")
    
    if user == str(number):
        print("Trouvé")
        break
    elif user < str(number):
        print("C'est +")
        chances = chances - 1
        print("Vous n'avez plus que", chances, "chances...")
    elif user > str(number):
        print("C'est -")  
        chances = chances - 1
        print("Vous n'avez plus que", chances, "chances...")
    if chances == 0:
        print("GAME OVER")
        print("La réponse était:",number)


