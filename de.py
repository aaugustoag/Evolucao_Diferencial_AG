from random import uniform
from random import randint
from random import sample

d = 2
dominio = [-30,30]
erro = 1

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

np = 10
cr = 0.7
f = 1
gen = 20

def diferencial (pop_dif, f):
  dif = [0]
  for i in range(len(pop_dif[0])-1):
    dif.append(round((pop_dif[0][i+1] - pop_dif[1][i+1]) * f, erro))
    dif[0] += round(dif[i+1]**2,erro)
  return dif

def mutacao (dif, pop_ruido):
  mut = [0]
  for i in range(len(dif)-1):
    mut.append(round((dif[i+1] + pop_ruido[i+1]) * f, erro))
    mut[0] += round(dif[i+1]**2,erro)
  return mut

def cruzamento (ruido, pop_cruzada):
  cruz = [0]
  for i in range(len(ruido)-1):
    if (i<(len(ruido)-1)/2):
      cruz.append(round(ruido[i+1], erro))
    else:
      cruz.append(round(pop_cruzada[i+1], erro))
    cruz[0] += round(cruz[i+1]**2,erro)
  return cruz

def selecao (experimental, pop_selecionada):
  if (experimental[0]<pop_selecionada[0]):
    return experimental
  else:
    return pop_selecionada

pop = gera_pop(np,d,dominio)

for j in range(gen):
  for i, ind in enumerate(pop):
    pop.remove(pop[i])
    pop_exp = sample(pop,3)
    pop_exp.append(ind)
    dif = diferencial (pop_exp[2:],f)
    ruido = mutacao (dif, pop_exp[1])
    experimental = cruzamento(ruido, pop_exp[0])
    pop.insert(i,selecao(experimental,ind))
    print(sorted(pop)[0])

print("\n",sorted(pop)[0])
