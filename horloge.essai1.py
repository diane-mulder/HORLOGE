import time 

def afficher_heure():

    heure = (16,59,40)
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
            break
        
        time.sleep(1)

               

afficher_heure()       



