import time
import keyboard
from datetime import datetime


# fonction affichage de l'heure actuel
def heure_actuel():
    global choix_mode_affichage

    # savoir qu'elle format d'heure on veut afficher.
    while True:
        choix_mode_affichage = input("choisissez votre mode d'affichage :\n 1.mode 24h\n 2.mode 12h\n")
        # permet de choisir le mode d'affichage
        if choix_mode_affichage == "1":
            break
        elif choix_mode_affichage == '2':
            date = str(datetime.now().time())
            date = date[:-7]
            # prendre les valeurs de la variable date pour le mettre dans une tuple
            heure = date[0:2]
            minute = date[3:5]
            seconde = date[6:]
            # mettre les valeur en mode int pour la suite
            heure = int(heure)
            minute = int(minute)
            seconde = int(seconde)
            # tuple date
            date = (heure, minute, seconde)
            afficher_heure(date)
            break
        else:
            continue

    while True:
        datetime.now().time()  # prend l'heure actuel
        date = str(datetime.now().time())  # on met l'heure actuel sous frome de str pour pouvoir enlever le micro
        # seconde par la suite
        date = date[:-7]  # on enlève les micro seconde le l'heure actuel  #
        print(date)
        pause()


# focntion qui prend heure modifié
def choix_heure():
    global choix_mode_affichage
    global choix  # pour savoir si on a chosit de mettre une alarme
    while True:
        heure_modifier = input("Entrer l'heure sous la forme HH:MM:SS : ")
        heure = int(heure_modifier[:2])
        minute = int(heure_modifier[3:5])
        seconde = int(heure_modifier[6:])

        # condition si l'heure entrée ne correspond pas
        if heure not in range(0, 24):
            print('votre heure est trop grande')
            continue
        if minute not in range(0, 60):
            print('les minutes que vous avez entrer ne corresponde pas')
            continue
        if seconde not in range(0, 60):
            print('Les secondes que vous avez entré ne corresponde pas')
            continue
        else:
            heure_modifier = (heure, minute, seconde)  # ajout de l'heure dans un TUPLE
            break
    # condition si on a chois de mettre l'alarme
    if choix == '3':
        alarme(heure_modifier)

    # savoir qu'elle format d'heure on décide d'afficher
    while True:
        choix_mode_affichage = input("choisissez votre mode d'affichage :\n 1.mode 24h\n 2.mode 12h\n")
        # permet de choisir le mode d'affichage
        if choix_mode_affichage == "1":
            break
        elif choix_mode_affichage == '2':
            break

    afficher_heure(heure_modifier)


# foonction affichage de l'heure modofié
def afficher_heure(heure_affichage):
    global choix_mode_affichage  # pour savoir qu'elle format d'heure on décide d'avoir
    # definition des variable pour faire avancer heure
    seconde = heure_affichage[2]
    minute = heure_affichage[1]
    heure = heure_affichage[0]
    heure_de_reference = heure

    # boucle qui actualise l'heure toutes les secondes
    while True:
        seconde = seconde + 1
        if seconde == 60:
            seconde = 0
            minute = minute + 1
        if minute == 60:
            minute = 0
            heure = heure + 1
        if heure == 24:
            heure = 0

        # mettre les valeurs en str pour affichage 00
        seconde = str(seconde)
        minute = str(minute)

        # permet de rajouter 0 au debut de la chaine de caractère si <10
        if len(seconde) < 2:
            seconde = list(seconde)
            seconde.insert(0, '0')
            seconde = "".join(seconde)

        if len(minute) < 2:
            minute = list(minute)
            minute.insert(0, '0')
            minute = "".join(minute)
        # condition si on veut afficher heure sous forme 12h
        if choix_mode_affichage == "2":
            # si l'heure est supéreieur a 13h on fait -12
            if heure >= 13:
                heure = heure - 12
                heure = str(heure)
                if len(heure) < 2:
                    heure = list(heure)
                    heure.insert(0, '0')
                    heure = "".join(heure)

            # si l'heure est inférieur a 12 pas de changement
            elif heure <= 12:
                heure = str(heure)
                if len(heure) < 2:
                    heure = list(heure)
                    heure.insert(0, '0')
                    heure = "".join(heure)

                # savoir si c'est AM ou PM
                if heure_de_reference >= 12:
                    print(heure + ":" + minute + ":" + seconde + "PM")

                if heure_de_reference < 12:
                    print(heure + ":" + minute + ":" + seconde + "AM")

        # condition pour afficher heure sous forme 24h
        if choix_mode_affichage == "1":
            heure = str(heure)
            if len(heure) < 2:
                heure = list(heure)
                heure.insert(0, '0')
                heure = "".join(heure)
            # affichage de l'haure
            print(str(heure) + ':' + str(minute) + ':' + str(seconde))

        # remettre les valeurs en int pour que la boucle recommence
        seconde = int(seconde)
        minute = int(minute)
        heure = int(heure)
        pause()


# fonction alarme
def alarme(heure_modif):
    global heure_modifier

    seconde = str(heure_modif[2])
    minute = str(heure_modif[1])
    heure = str(heure_modif[0])

    if len(seconde) < 2:
        seconde = list(seconde)
        seconde.insert(0, '0')
        seconde = "".join(seconde)

    if len(minute) < 2:
        minute = list(minute)
        minute.insert(0, '0')
        minute = "".join(minute)

    if len(heure) < 2:
        heure = list(heure)
        heure.insert(0, '0')
        heure = "".join(heure)

    # permet de définir l'heure de l'arme sous forme de str
    heure_alarme = (heure + ':' + minute + ':' + seconde)

    # condition qui affiche message quand heure actuelle == heure de l'alarme
    while True:
        date = list(str(datetime.now().time()))
        date = date[:-7]
        date = "".join(date)

        if date == heure_alarme:
            print('--------------')
            print("Hey Wake up is : ")
            print(heure_alarme)
            print('---------------')
            menu()
            break
        else:
            time.sleep(1)
            continue


# focntion pour mettre en pause
def pause():
    running = True
    display = True
    block = False

    while running:
        time.sleep(1)  # actualise toute les 1 seconde
        if keyboard.is_pressed("delete"):  # si touche presser
            print("Pause")
            if block == False:
                display = not display
                block = True
                print('Appuyer sur la touche delete pour reprendre.')
        else:
            block = False  # permet de remetre la fcontion if si on remet pause
        if display:
            return  # retourne a la focntion affier_heure si la touche n'est pas pressé


# fonction menu
def menu():
    global choix
    while True:
        entrer = input("Bienvenue sur le menu  de l'horloge, appuyer sur ENTRER pour continuer : ")
        if entrer == '':
            break
    print('faites votre choix :\n 1.Afficher heure actuel\n 2.Afficher une heure modifier \n 3.Mettre une alarme')

    while True:
        choix = input('')
        if choix == '1':
            heure_actuel()
        elif choix == '2':
            choix_heure()
        elif choix == '3':
            choix_heure()
            alarme()
        else:
            continue


menu()
