import time
from tkinter import *
from tkinter import messagebox
import webbrowser

running = True

start_app = input('Pour démarrer le bot il faut dire start dans ce message : ')

print("Pour voir la chaine youtube du créateur vous devez taper /youtube")


print("Pour voir la chaine twitch du créateur vous devez taper /twitch ")

if 'start' in start_app:

    while running:    
        
        
        enter = input('Entrer votre commande : ')
        
        
        
        
        if "help" in enter:
            print('voici les commandes :')
            
            print("/youtube")

            print("/twitch")

            print('quitte : permet de quitter la boucle')


        elif "/youtube" in enter:
            webbrowser.open('https://www.youtube.com/@lamalice2.0')

        elif '/twitch' in enter:
            webbrowser.open('https://twitch.tv/lamalice20')

        elif 'quitte' in enter:
            running = False




