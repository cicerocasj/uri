resto = float(input())
t = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0,
     1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
d = {}
for teste in t:
    d[teste] = 0
i = 0
while resto > 0 and i < len(t):
    d[t[i]] = resto // t[i]
    resto = resto % t[i]
    i += 1
print 'NOTAS:'
print '%d nota(s) de R$ 100.00' % (d[t[0]])
print '%d nota(s) de R$ 50.00' % (d[t[1]])
print '%d nota(s) de R$ 20.00' % (d[t[2]])
print '%d nota(s) de R$ 10.00' % (d[t[3]])
print '%d nota(s) de R$ 5.00' % (d[t[4]])
print '%d nota(s) de R$ 2.00' % (d[t[5]])
print 'MOEDAS:'
print '%d moeda(s) de R$ 1.00' % (d[t[6]])
print '%d moeda(s) de R$ 0.50' % (d[t[7]])
print '%d moeda(s) de R$ 0.25' % (d[t[8]])
print '%d moeda(s) de R$ 0.10' % (d[t[9]])
print '%d moeda(s) de R$ 0.05' % (d[t[10]])
print '%d moeda(s) de R$ 0.01' % (d[t[11]])
