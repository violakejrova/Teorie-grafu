
import pandas as pd
import numpy as np
from sympy import Matrix


n = 9999
mesta = ('Praha', 'Brno', 'Litoměřice', 'Pardubice', 'Kroměříž')

s = [(0, 207, 70, 125, 267),
    (n, 0, 274, n, 44),
    (70, n, 0, 176, n),
    (124, 146, n, 0, n),
    (n, n, 337, 192, 0)]
display (Matrix(s))

vzdalenost = np.array(s)

def alg(s):
  for i in range((len(mesta))):
      for j in range(len(mesta)):
          for k in range(len(mesta)):
              vzdalenost[i][j] = min(vzdalenost[i][j], vzdalenost[i][k] + vzdalenost[k][j])

  return vzdalenost


print('\n', 'konečná tabulka: ', '\n')
display (Matrix(alg(s)))
display (pd.DataFrame(alg(s), mesta, mesta))

a = alg(s)
#a = list (alg(s))
start = input('start: ')
cil = input('cíl:  ')
i = mesta.index(start)
j = mesta.index(cil)
print (a[i][j], 'km')


for k in range(len(mesta)):
  if a[i][k] + a[k][j] == a[i][j]:
    print ('cesta vede přes', mesta [k])

