# -*- coding: utf-8 -*-
entrada = str(raw_input()).split(" ")
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

x = (a + b + abs(a-b))/2
x = (x + c + abs(x-c))/2
print "%d eh o maior" % x
