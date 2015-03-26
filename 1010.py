# -*- coding: utf-8 -*-
a = str(raw_input()).split(" ")
b = str(raw_input()).split(" ")

print "VALOR A PAGAR: R$ %.2F" % (float(a[1]) * float(a[2]) + float(b[1]) * float( b[2]))
