import time 
import os
import winsound


def afficher_heure():

    heure = (16,59,50)
    heure_list = list(heure)
    alarme = (17,00,00)
    alarme_list = list(alarme)

    while True:
        heure_list[2] += 1
        if int(heure_list[2]) == 60:
            heure_list[2] = 0
            heure_list[1] += 1
            if int(heure_list[1]) == 60:
                heure_list[1] = 0
                heure_list[0] += 1
        print(f"{heure_list[0]:02}:{heure_list[1]:02}:{heure_list[2]:02}")

        if alarme_list == heure_list:
            print("c'est l'heure de se reveiller!")
            os.system('afplay alarm.wav') # Joue le son de l'alarme (sur MacOS)
            break
        
        time.sleep(1)

               
afficher_heure()     


def play_alarm():
    duration = 1000  # durée du son en millisecondes
    freq = 500  # fréquence du son en hertz
    for i in range(10):  # jouer le son 10 fois
        winsound.Beep(freq, duration)
        time.sleep(0.1) 


play_alarm()
