
#region NUMPY
"""import numpy as np 
np.cos
np.sin
np.tan
np.pi
np.e
np.exp(x) for exponents of e (e^x)

a = 3 #starting value
b = 8 #ending value
n = 50 #amount of pieces
inclusiveb = True #toggles whether b will be included or not
interval = np.linspace(a, b, n, inclusiveb) #makes a list of values from a (always inclusive) to b (toggle inclusivity), divided into dx equal pieces, useful for integration 
#linspace is best if a and b are integers


dx = 0.1 #length of each step
interval = np.arange(a,b, dx) #makes a list of values from a (inclusive) to b (exclusive), with a defined length step between each value
#arange is best if a and b are decimals
"""

#endregion

#region RANDOM
import random




#endregion

#region MATPLOTLIB.PYPLOT
import matplotlib.pyplot as plt 

#region DATA INPUT:
xlist = [] #list with x values of points
ylist = [] #list with y values of points
#endregion

#region DATA PLOT FORMATTING
format = "" #string describing the format of the points and line between them
#written as "<marker><line><color>", e.g. "or--" for o markers that are red connected by dashed line

#region Markers
# '.'  point marker
# ','  pixel marker
# 'o'  circle marker
# 'v'  triangle_down marker
# '^'  triangle_up marker
# '<'  triangle_left marker
# '>'  triangle_right marker
# '1'  tri_down marker
# '2'  tri_up marker
# '3'  tri_left marker
# '4'  tri_right marker
# '8'  octagon marker
# 's'  square marker
# 'p'  pentagon marker
# 'P'  plus (filled) marker
# '*'  star marker
# 'h'  hexagon1 marker
# 'H'  hexagon2 marker
# '+'  plus marker
# 'x'  x marker
# 'X'  x (filled) marker
# 'D'  diamond marker
# 'd'  thin_diamond marker
# '|'  vline marker
# '_'  hline marker
#endregion
#region Line Styles
# '-'  solid line style
# '--'  dashed line style
# '-.'  dash-dot line style
# ':'   dotted line style
#endregion
#region Colours
# 'b'  blue
# 'g'  green
# 'r'  red
# 'c'  cyan
# 'm'  magenta
# 'y'  yellow
# 'k'  black
# 'w'  white
#endregion

functionlabel = "" #name of the function for the legend

#endregion


#plt.plot command plots points for each index in the lists, taking the x value from the first and y value from the second list.
if len(xlist) == len(ylist): 
    plt.plot(xlist, ylist, format, label=functionlabel)
else:
    raise ValueError("Lists to be plotted are not equal in length")

#note that you can make a list of functions in python and plot them all with a for loop!

plt.legend() #to show the legend
plt.bar(x, y, dx, align="edge") 
#Plots a bar; x axis location, height, width, alignment with x ("edge" for left; default center, negative value for width for right), 


#region AXIS FORMATTING
xstartvalue = -10
xendvalue = 10
ystartvalue = -10
yendvalue = 10

plt.xlim(xstartvalue, xendvalue)
plt.ylim(ystartvalue, yendvalue)

xaxislabel = "time" #for example
yaxislabel = "height"

plt.xlabel(xaxislabel)
plt.ylabel(yaxislabel)

a=1 #example values
b=2
plt.axhline(y=a, color="r") #draws a line at the specified y value and colour, parallel to the x axis
plt.axvline(x=b, color="k") #draws a line at the specified x value and colour, parallel to the y axis

#endregion


plt.show() #DISPLAYS THE MASTERPIECE

#endregion