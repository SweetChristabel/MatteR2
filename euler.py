# OWN ATTEMPT
"""
x = 0 # x ved starten
y = 200 # y ved starten
d = 0.5 # endring

while x <= 100:
    y += (10-0.15*y)*d
    x += d
    print(f" x {x}  y {y} ")




# SCHOOL TEACHINGS



n = 20 #antall punkter/iterasjoner

x = zeros(n) #lager en array med n 
y = zeros(n)

x[0] = 0 # x ved starten
y[0] = 200 # y ved starten 
dx = 0.5  #endring

for i in range (n-1):
    x[i+1] = x[i] + dx #endring i x
    y[i+1] = y[i] + (10-0.15*y[i])*dx #endring i y

plot(x,y)
show()


#ANOTHER EXAMPLE WITH DOUBLE DIFFERENTIATION
#harmonisk svinging

from pylab import *

m = 2 #masse, 2 kilo
k = 1 #fjærkonstant - jo større jo stivere


#INITIAL VALUES
n = 40000 #antall punkter
t = zeros(n) #tid
s = zeros(n) #posisjon
ds = zeros(n) #speed (differentiated once)
dds = zeros(n)  #acceleration (differentiated twice)
dx = 0.001

t[0] = 0
s[0] = -0.5 #posisjon ved start (er det 0 så blir det ikke noe bevegelse, ykno)
ds[0] = 0
dds[0] = -k*s[0]/m

for i in range (n-1):
    s[i+1] = s[i] + ds[i] * dx
    ds[i+1] = ds[i] + dds[i] * dx
    dds[i+1] = -k*s[i+1]/m
    t[i+1] = t[i]+dx     

plot(t,s)
show()
"""

#DEMPENDE SVINGING - den eneste forskjellen er at nå har vi en q verdi som vi har satt inn i formelen.
#Vurder å definere formelen som en funksjon.

from pylab import *

m = 2 #masse, 2 kilo
k = 1 #fjærkonstant - jo større jo stivere
q = 0.2

#INITIAL VALUES
n = 80000 #antall punkter
t = zeros(n) #tid
s = zeros(n) #posisjon
ds = zeros(n) #speed (differentiated once)
dds = zeros(n)  #acceleration (differentiated twice)
dx = 0.001

t[0] = 0
s[0] = -0.5 #posisjon ved start (er det 0 så blir det ikke noe bevegelse, ykno)
ds[0] = 0
dds[0] = -(q*ds[0]+k*s[0])/m

for i in range (n-1):
    s[i+1] = s[i] + ds[i] * dx
    ds[i+1] = ds[i] + dds[i] * dx
    dds[i+1] = -(q*ds[i+1]+k*s[i+1])/m
    t[i+1] = t[i]+dx     

plot(t,s)
show()
