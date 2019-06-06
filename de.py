from random import uniform
from random import randint
from random import sample

d = 4
dominio = [-30,30]
erro = 3

def gera_ind_aleatorio (d,dominio):
  ind = [0]
  for i in range(d):
    ind.append(round(uniform(dominio[0],dominio[1]),erro))
    ind[0] += round(ind[i+1]**2, erro)
  return ind

def gera_pop (np, d, dominio):
  pop = []
  for i in range(np):
    pop.append(gera_ind_aleatorio (d,dominio))
  return pop

np = 5
cr = 0.7
f = 1
gen = 20

def mutacao (dif, pop_ruido):
  mut = []
  return mut

def diferencial (pop_dif, f):
  dif = [0]
  for i in range(len(pop_dif[0])-1):
    dif.append((pop_dif[0][i+1] - pop_dif[1][i+1]) * f)
    dif[0] += round(dif[i+1]**2,erro)
  return dif

pop_exp = []
pop = gera_pop(np,d,dominio)
for i in range(3):
  pop_exp = sample(0,len(pop)-1,4)

dif = diferencial (pop_exp[2:])
ruido = mutacao (dif, pop_exp[1])

print(dif,"\n",ruido)
