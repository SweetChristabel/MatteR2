import numpy as np

def f(x):
    return x**2-x+4

a=3    #nedre grense
b=7    #øvre grense
N=50 # startantall rektangler
precision = 0.1 #nøyaktighet

def numintegralrectangle(antallrektangler: int, nedregrense: int, øvregrense:int, funksjon, kalk: int):
    S= 0 #startsum
    dx = (øvregrense - nedregrense)/antallrektangler
    for i in range(antallrektangler):
        if kalk == 1: #Venstrestilt
            H = funksjon(nedregrense+i*dx)
        elif kalk == 2: #Midtstilt
            H = funksjon(nedregrense+(i+0.5)*dx)
        elif kalk == 3: #Høyrestilt
            H = funksjon(nedregrense+(i+1)*dx)
        else:
            raise ValueError("Unknown calculation")
        A = H * dx #areal av rektangel
        S += A #legg til summen
    return S

def numintegraltrapeze(antalltrapeser, nedregrense, øvregrense, funksjon):
    S= 0 #startsum
    dx = (øvregrense - nedregrense)/antalltrapeser
    for i in range(antalltrapeser):
        h1 = funksjon(a+i*dx)
        h2 = funksjon(a+(i+1)*dx)
        A = (h1*dx+h2*dx)/2
        if i % 100 == 0:
            print(f"areal: {A} sum: {S}")
        S += A
    return S

def approachprecision(difference, function, precision):
    #while difference > precision:
    pass



upper = numintegralrectangle(N, a, b, f, 3)
lower = numintegralrectangle(N, a, b, f, 1)
diff = upper-lower

while diff > precision:
    N+= 1
    upper = numintegralrectangle(N, a, b, f, 3)
    lower = numintegralrectangle(N, a, b, f, 1)
    diff = upper - lower
    if diff > 50000: # unngå å brenne opp PCen hvis man gjør noe feil
        raise ValueError("Difference between upper and lower limit too big")
    
trapez = numintegraltrapeze(N, a, b, f)

print(f"""Rectangle lower: {lower}
Rectangle upper: {upper}
Final difference: {diff}
Trapezoid: {trapez}
Amount of shapes: {N}""")