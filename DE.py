from random import uniform
from random import sample
import matplotlib.pyplot as plt

d = 2
dominio = [-10,10]
erro = 10

def gera_ind_aleatorio (d,dominio):
  ind = [0]
  for i in range(d):
    ind.append(uniform(dominio[0],dominio[1]))
    ind[0] += ind[i+1]**2
  return ind

def gera_pop (np, d, dominio):
  pop = []
  for i in range(np):
    pop.append(gera_ind_aleatorio (d,dominio))
  return pop

np = 10
cr = 0.7
f = 0.9
gen = 30
def diferencial (pop_dif, f):
  dif = [0]
  for i in range(len(pop_dif[0])-1):
    dif.append((pop_dif[0][i+1] - pop_dif[1][i+1]) * f)
    dif[0] += dif[i+1]**2
  return dif

def mutacao (dif, pop_ruido):
  mut = [0]
  for i in range(len(dif)-1):
    mut.append((dif[i+1] + pop_ruido[i+1]) * f)
    mut[0] += dif[i+1]**2
  return mut

def cruzamento (ruido, pop_cruzada):
  cruz = [0]
  for i in range(len(ruido)-1):
    if (i<(len(ruido)-1)/2):
      cruz.append(ruido[i+1])
    else:
      cruz.append(pop_cruzada[i+1])
    cruz[0] += cruz[i+1]**2
  return cruz

def selecao (experimental, pop_selecionada):
  if (experimental[0]<pop_selecionada[0]):
    return experimental
  else:
    return pop_selecionada

pop = gera_pop(np,d,dominio)
convergencia = []
convergencia2 = []

for j in range(gen):
  for i, ind in enumerate(pop):
    pop.remove(pop[i])
    pop_exp = sample(pop,3)
    pop_exp.append(ind)
    dif = diferencial(pop_exp[2:],f)
    ruido = mutacao(dif, pop_exp[1])
    experimental = cruzamento(ruido, pop_exp[0])
    pop.insert(i,selecao(experimental,ind))
  convergencia.append((sorted(pop)[0][0])**(1/2))
  convergencia2.append((sorted(pop)[-1][0])**(1/2))

print("\n",sorted(pop)[0])

# plota curvas de convergencia
plt.figure('Convergencia', figsize=(9, 6))
plt.plot(convergencia, 'b')
plt.plot(convergencia2, 'r')
plt.xlabel("Geracoes")
plt.ylabel('Valor')
plt.show()
# fim