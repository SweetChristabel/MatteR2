import pylab
import numpy as np
import random
vismeggrafen = False #True hvis en graf skal tegnes; juster detaljer under visualisering

def f(x):
    #placeholder for en funksjon
    pass

#region NUMERISK INTEGRASJON  - FERDIG
def trapes(verdi1, verdi2, dx): #Beste metoden for ujevne intervaller, nesten-linear/log funksjoner og måledata
    return ((verdi1+verdi2)/2)*dx

def rektangelmid(funksjon: callable, startX, dx): #Brukes kun hvis man har en funksjon, best for symmetriske funksjoner (sin, exp)
    return funksjon(startX+dx/2)

def rektangelkant(verdi1, verdi2, dx, side: bool = False): #VENSTRESTILT FALSE, HØYRESTILT TRUE
    if side:
        return verdi2*dx
    else:
        return verdi1*dx

#endregion

def dataintegralsummering(metode: callable, xlist, ylist, startsum=0):
    for i in range(len(xlist)):
        dx = xlist[i]
        verdi1 = ylist[i]
        verdi2 = ylist[i+1]
        startsum += metode(verdi1, verdi2, dx) #husk å tilsette True hvis høyrestilt rektangel
        print(dx, verdi1, verdi2, startsum)
    return startsum



x = [2.4,2.7,2.8,2.7,1.4]
y = [11.19,10.88,9.77,7.88,5.48,4.06]


print(dataintegralsummering(trapes, x, y)*2) #ganger med to fordi jeg skal også ha med arealet under x-aksen
