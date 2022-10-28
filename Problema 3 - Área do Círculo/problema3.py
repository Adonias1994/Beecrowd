#coding: utf-8
#A fórmula da área do círculo é area = n.raiox2, onde n = 3.14159
n = 3.14159
#Poderia ser utilizado a = 'A='
raio = float(input())
''' 
O certo em pontencia seria usar raio ** n
onde n seria o número da pontencia
'''
area = n * raio * raio
'''
Limita o número de casas decimais após o ponto
area1 = round(area, 4) mas vamos utilizar outra forma
---
Poderia ser utilizado caso fosse usado a variável a = 'A='
print(a + str(area1))
'''
print('A=%.4f' % area)
