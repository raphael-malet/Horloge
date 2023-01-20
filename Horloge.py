import time
from datetime import datetime



#fonction affichage de l'heure actuel
def heure_actuel():
    while True:
        datetime.now().time() #prend l'heure actuel
        date = list(str(datetime.now().time())) # on met l'heure actuel sous frome de liste pour pouvoir enlever le micro seconde par la suite
        date = date[:-7]#on enlève les micro seconde le l'heure actuel
        date = "".join(date)#on remet l'here en str
        print(date)
        time.sleep(1)

    
 
#focntion qui prend heure modifié 
def modifier_heure():
    global heure_modifier
    while True:
        heure_modifier = input("Entrer l'heure sous la forme HH:MM:SS : ")
        heure = int(heure_modifier[:2]) 
        minute = int(heure_modifier[3:5])
        seconde = int(heure_modifier[6:])
        
        #condition si l'heure entrée ne correspond pas
        if heure not in range(0,24) :
            print('votre heure est trop grande')
            continue
        if minute not in range(0,60) :
            print('les minutes que vous avez entrer ne corresponde pas')
            continue
        if seconde not in range(0,60):
            print('Les secondes que vous avez entré ne corresponde pas')
            continue
        else:
            heure_modifier = (heure, minute, seconde)#ajout de l'heure dans un TUPLE
            break
        
#foonction affichage de l'heure modofié
def afficher_heure():
    global heure_modifier
    
    seconde = heure_modifier[2]
    minute = heure_modifier[1]
    heure = heure_modifier[0]
    
    #boucle qui actualise l'heure toutes les secondes
    while True :
        seconde = seconde + 1
        if seconde == 60:
            seconde = 0
            minute = minute + 1
        if minute == 60 : 
            minute = 0
            heure = heure + 1
        if heure == 24 : 
            heure = 0
        
        #mettre les valeurs en str pour affichage 00
        seconde = str(seconde)
        minute = str(minute)
        heure = str(heure)
        
        
        if len(seconde) <2 :
            seconde = list(seconde)
            seconde.insert(0, '0')
            seconde = "".join(seconde)
        
        if len(minute) <2 :
            minute = list(minute)
            minute.insert(0, '0')
            minute = "".join(minute)
            
        if len(heure) <2 :
            heure = list(heure)
            heure.insert(0, '0')
            heure = "".join(heure)
        

        print(heure + ':' + minute + ':' + seconde)
        
        #permet de remettre les valeurs en int pour reprendre la boucle    
        seconde = int(seconde)
        minute = int(minute)
        heure = int(heure)        
        
        time.sleep(1)
    
def alarme():
    global heure_modifier
 
    seconde = str(heure_modifier[2])
    minute = str(heure_modifier[1])
    heure = str(heure_modifier[0])
    
    if len(seconde) <2 :
            seconde = list(seconde)
            seconde.insert(0, '0')
            seconde = "".join(seconde)
        
    if len(minute) <2 :
            minute = list(minute)
            minute.insert(0, '0')
            minute = "".join(minute)
            
    if len(heure) <2 :
            heure = list(heure)
            heure.insert(0, '0')
            heure = "".join(heure)
        

    heure_alarme = (heure + ':' + minute + ':' + seconde)
    
    

    while True:
        date = list(str(datetime.now().time())) 
        date = date[:-7]
        date = "".join(date)
        
        if date == heure_alarme:
            print('--------------')
            print(heure_alarme)
            print('---------------')
            menu()
            break
        else: 
            time.sleep(1)
            continue
   
        
            

def menu():
    
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
            modifier_heure()
            afficher_heure()
        elif choix == '3':
            modifier_heure()
            alarme()
        else:
            continue    
    
menu()