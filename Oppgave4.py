import numpy as np
import matplotlib.pyplot as plt 
a = 100
b = 100
suma = 0
sumb = 0

def tilbud1(a):
    return a+10

def tilbud2(b):
    return b*1.05

for i in range(1,5):
    print(f"a) I uke {i} får David {a}kr med tilbud 1 eller {round(b,2)}kr med tilbud 2.")
    a = tilbud1(a)
    b = tilbud2(b)
    

a = 100 
b = 100

for i in range(1,50):
    if b > a: #stopper løkka når og skriver ut svaret når den er funnet
        print(f"b) I uke {i} gir tilbud 2 ({round(b,2)}) mer enn tilbud 1 ({a})")
        break
    a = tilbud1(a)
    b = tilbud2(b)


a = 100 
b = 100
suma = 0
sumb = 0

for i in range(50):
    if sumb > suma:
        print(f"c) I uke {i} har tilbud 2 ({round(sumb,2)}) lønnet seg over tilbud 1 ({suma})")
        break
    suma += a
    a = tilbud1(a)
    sumb += b
    b = tilbud2(b)
    

