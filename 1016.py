a = int(input())
x,y = 0,0
i = 0
while (y - x) < a:
    x += 1
    y += 1.5
    i += 1

print '%d minutos' % i
