import time 

def afficher_heure():

    heure = (16,59,40)
    heure_list = list(heure)
    alarme = (17,59,00)
    alarme_list = list(alarme)

    while True:
        heure_list[2] += 1
        if int(heure_list[2]) == 60:
            heure_list[2] = 0
            heure_list[1] += 1
            if int(heure_list[1]) == 60:
                heure_list[1] = 0
                heure_list[0] += 1
        print(f"{heure_list[0]}:{heure_list[1]}:{heure_list[2]}")
        
        time.sleep(1)

        if int(alarme_list)[2] ==60:
            alarme_list[2] = 0
            



afficher_heure()       



                

   


