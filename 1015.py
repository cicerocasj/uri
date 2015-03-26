# -*- coding: utf-8 -*-
from math import sqrt
entrada1 = str(raw_input()).split(" ")
a = float(entrada1[0])
b = float(entrada1[1])
entrada2 = str(raw_input()).split(" ")
c = float(entrada2[0])
d = float(entrada2[1])
x = c - a
y = d - b
print "%.4f" % sqrt((x*x)+(y*y))
