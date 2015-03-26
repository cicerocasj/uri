# -*- coding: utf-8 -*-
entrada = str(raw_input()).split(" ")
a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

print "TRIANGULO: %.3f" % (a * c / 2.0)
print "CIRCULO: %.3f" % (c * c * 3.14159)
print "TRAPEZIO: %.3f" % ((c*(b+a)) / 2.0)
print "QUADRADO: %.3f" % (b * b)
print "RETANGULO: %.3f" % (a * b)
