import sys

def abreparen(paren):
  if paren == "(":
    return True
  else:
    return False


def fechaparen(paren):
  if paren == ")":
    return True
  else:
    return False


def constante(letra):
  if (letra == "T") or (letra == "F"):
    return True
  else:
    return False


def preposicao(letras):
  if all(letra.isdigit() or letra.islower() for letra in letras):
    return True
  else:
    return False


def operadorunario(nao):
  if nao == r"\neg":
   return True
  else:
    return False

def operadorbinario(operador):
  if (operador == r"\lor" or operador == r"\land" or operador == r"\Rightarrow" or operador == r"\Leftrightarrow"):
   return True
  else:
    return False
  
def formulabinaria(exprecao):
  auxoperador = 0
  if exprecao[4] == 'r':
    auxoperador = 5
  elif exprecao[4] == 'n':
    auxoperador = 6
  elif exprecao[4] == 'g':
    auxoperador = 12
  elif exprecao[4] == 'f':
    auxoperador = 16
  else:
    return False
  auxformula = 0
  if exprecao[auxoperador] == "(":
    auxformula = exprecao[auxoperador:].find(")") + 1
  elif exprecao[auxoperador] == "T" or exprecao[auxoperador] == "F":
    auxformula = auxoperador + 1
  else:
    auxformula = exprecao[auxoperador].find("(")
    if auxformula == -1:
      auxformula = len(exprecao)-2
    
  if (abreparen(exprecao[0]) and operadorbinario(exprecao[1:auxoperador]) and formula(exprecao[auxformula:len(exprecao)-1]) and formula(exprecao[auxformula:len(exprecao)-1]) and fechaparen(exprecao[len(exprecao)-1])):
    return True
  else:
    return False  

def formulaunaria(exprecao):
  if (abreparen(exprecao[0]) and operadorunario(exprecao[1:5]) and formula(exprecao[5:len(exprecao)-1]) and fechaparen(exprecao[len(exprecao)-1])):
    return True
  else:
    return False


def formula(exprecao):
  if(constante(exprecao) or preposicao(exprecao) or formulaunaria(exprecao) or formulabinaria(exprecao)):
    return True
  else:
    return False



def parser(exprecao):
  if formula(exprecao):
    return "Valida"
  else:
    return "Invalida"
  


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    primeiro = True
    for line in lines:
      texto = line.strip('\n')
      if primeiro:
        n_formulas = int(texto)
        primeiro = False
      elif n_formulas > 0:
        print(parser(texto))
        n_formulas -= 1 
      else:
        break