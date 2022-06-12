#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math
from time import sleep
"""
Rappel : indice réfraction air : 1 (ou presque)
indice réfraction verre : 1,5 (en moyenne)
indice réfraction eau : 1,33333 (4/3)
"""
def foncTransmis():
    n1=float(input("Entrez l'incide de réfraction du premier milieu : "))
    n2=float(input("Entrez l'incide de réfraction du second milieu : "))
    angl1=float(input("Entrez l'angle d'incidence en degrés "))
    angle1=math.pi*angl1/180
    print("Vous avez entré",angl1,"° soit",angle1,"rad.")
    if n2<n1:
        anglim=abs(math.asin(n2/n1))
    else:
        anglim=math.pi/2
    print("iL =",anglim,'rad',)
    if angle1==anglim:
        print("L'angle de réfraction est \u03B8t = 90 \u00B0")
    elif angle1>anglim:
        print("Ce calcul est impossible, il y aura réflexion complète.")
    else:
        angl2=abs(math.asin(math.sin(angle1)*n1/n2))*180/math.pi
        print("L'angle",angl1,"° incident sortira avec un angle",angl2,"°.")
    return(True)

def foncIncident():
    n1=float(input("Entrez l'incide de réfraction du premier milieu : "))
    n2=float(input("Entrez l'incide de réfraction du second milieu : "))
    angl2=float(input("Entrez l'angle de réfraction en degrés "))
    angle2=math.pi*angl2/180
    if n1<n2:
        anglim=abs(math.asin(n1/n2))
    else:
        anglim=math.pi/2
    if angle2==anglim:
        print("L'angle de réfraction est \u03B8t = 90 \u00B0")
    elif angle2>anglim:
        print("Ce calcul est impossible, il y aura réflexion complète.")
    else:
        angl1=abs(math.asin(math.sin(angle2)*n2/n1))*180/math.pi
        print("L'angle",angl2,"° transmis est issu d'un angle",angl1,"° incident.")
    return(True)

def foncIndiceDeux():
    n1=float(input("Entrez l'indice de réfraction du milieu incident. "))
    angli=float(input("Entrez l'angle d'incidence en degrés : "))
    anglt=float(input("Entrez l'angle de transmission en degrés : "))
    if anglt%180==0:
        print("Calcul impossible, division par zéro")
    else:
        n2=n1*math.sin(angli*math.pi/180)/math.sin(anglt*math.pi/180)
        print("L'indice de réfraction du 2eme milieu vaut",n2)
    return(True)

def foncIndiceUn():
    n2=float(input("Entrez l'indice de réfraction du milieu incident. "))
    angli=float(input("Entrez l'angle d'incidence en degrés : "))
    anglt=float(input("Entrez l'angle de transmission en degrés : "))
    if angli%180==0:
        print("Calcul impossible, division par zéro")
    else:
        n1=n2*math.sin(anglt*math.pi/180)/math.sin(angli*math.pi/180)
        print("L'indice de réfraction du 2eme milieu vaut",n2)
    return(True)


boucler=True

while boucler:
    print("")
    print("Menu principal")
    print("==============")
    print("")
    print("Veuillez saisir un choix et valider.")
    print("[1] : Calcul angle transmis")
    print("[2] : Calcul angle incident")
    print("[3] : Calcul indice réfraction milieu 2")
    print("[4] : Calcul indice réfraction milieu 1")
    print("[q] : Quitter")
    choix=input("> ")
    if choix=='1':
        foncTransmis()
    elif choix=='2':
        foncIncident()
    elif choix=='3':
        foncIndiceDeux()
    elif choix=='4':
        foncIndiceUn()
    elif choix=='42':
        print("Vous avez la réponse ...")
        boucler=True
    elif choix=='q':
        print("Vous avez choisi de nous quitter, au revoir.")
        boucler=False
    else:
        print("Saisie erronée, avez-vous vérifié le blocage des majuscules ?")
print("(c) F.S.G. Juin 2022")