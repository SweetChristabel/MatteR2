#skript skrevet for å forstå forskjellen mellom mitt svar og fasitsvar i en oppgave

import math

hcone = 15
rcone = 5

def cylindervolume(radius, height):
    return math.pi*(radius**2)*height

def simonasformel(n):
    radius = n * 5
    height = (1-n) * 15
    return radius, height

def fasitformel(radius):
    return 15-3*radius

dx = 1/1000
As = 0
Vs = 0

while dx < 1:
    x, y = simonasformel(dx)
    An = x * y
    Vn = cylindervolume(x, y)
    if An > As:
        axs = x
        ays = y
        As = An
        na = dx

    if Vn > Vs:
        vxs = x
        vys = y
        Vs = Vn
        nv = dx        

    dx += 1/1000

dx = 1/1000
Af = 0
Vf = 0

while dx < rcone:
    x = dx
    y = fasitformel(x)
    A = x * y
    V = cylindervolume(x, y)
    if A > Af:
        axf = x
        ayf = y
        Af = A

    if V > Vf:
        vxf = x
        vyf = y
        Vf = V
    
    dx += 1/1000



print(f"""
    ***Simonas løsning***
    x ved største rektangelareal {round(axs, 2)}
    y ved største rektangelareal {round(ays, 2)}
    største rektangelareal {round(As, 2)}
    n-verdi ved største rektangelareal {round(na, 2)}
    
    x ved største sylindervolum {round(vxs,2)}
    y ved største sylindervolum {round(vys,2)}
    største sylindervolum {round(Vs, 2)}
    n-verdi ved største sylindervolum {round(nv, 2)}

    ***fasitløsning*** 
    x ved største rektangelareal {round(axf, 2)}
    y ved største rektangelareal {round(ayf, 2)}
    største rektangelareal {round(Af, 2)}

    x ved største sylindervolum {round(vxf, 2)}
    y ved største sylindervolum {round(vyf, 2)}
    største sylindervolum {round(Vf, 2)}


    """)
