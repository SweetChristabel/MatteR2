"""
HÅNDBOK
dx = intervall/endring på x-aksen
verdi1 = verdi ved lavere x
verdi2 = verdi ved høyere x
"""
import pylab
import numpy as np
import random



vismeggrafen = False #True hvis en graf skal tegnes; juster detaljer under visualisering

def f(x):
    #placeholder for en funksjon
    pass

#region NUMERISK INTEGRASJON  - FERDIG
def trapes(verdi1, verdi2, dx): #Beste metoden for ujevne intervaller, nesten-linear/log funksjoner og måledata
    return (verdi1+verdi2)/2*dx

def rektangelmid(funksjon: callable, startX, dx): #Brukes kun hvis man har en funksjon, best for symmetriske funksjoner (sin, exp)
    return funksjon(startX+dx/2)

def rektangelkant(verdi1, verdi2, dx, side: bool = False): #VENSTRESTILT FALSE, HØYRESTILT TRUE
    if side:
        return verdi2*dx
    else:
        return verdi1*dx

#endregion
#region REKKER OG FØLGER
#region VISUALISERING - FERDIG
"""
Farger: g - green, k - black, r - red, b - blue, c - cyan, m - magenta, y - yellow (dark)
Linjer: - solid : dots -- dashes -. dash dot
Punkter: ., o, x, *
"""
if vismeggrafen:
    import matplotlib.pyplot as plt
    vislegende = False
    xaxis = "X" #gir aksen et navn
    yaxis = "Y"

    def plotenlinje(x,y,farge="k",linje="-",punkt="o",label:str=None): 
        form = farge+linje+punkt
        plt.plot(x,y,form,label=label)
    #x og y må være array/list
    #hvis man hopper over input må følgende inputs gis eksplisitt, f eks label="fart"

    if vislegende:
        plt.legend()

    plotenlinje("PLACEHOLDER")

    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.show()
#endregion
#region EULERS METODE

#endregion





""" FINE TUNE SLØYFER/REKURSJONER, SE OM DET KAN SLÅS SAMMEN MED REKKER/FØLGER"""
"""BLA GJENNOM KURSET FOR Å SE OM NOE ER GLEMT"""
def dataintegralsummering(metode: callable, xlist, ylist, startsum=0):
    i=0
    for i in range(len(xlist)-1): #For gitte x-verdier. Hvis intervallene er gitt, juster!
        dx = xlist[i+1]-xlist[i] #For gitte x-verdier. Hvis intervallene er gitt, juster!
        verdi1 = ylist[i]
        verdi2 = ylist[i+1]
        startsum += metode(verdi1, verdi2, dx) #husk å tilsette True hvis høyrestilt rektangel
    return startsum

#EKSEMPEL SOM FUNGERER; kan brytes opp for mer clarity som jeg har gjort over
#for i in range(len(tid)-1):
#    dx = tid[i+1]-tid[i]
#    total += rektangelkant(fart[i], fart[i+1], False, dx)