#Atividade da disciplina de Fundamentos da Programação, S1 do curso de Ciência da Computação
#O objetivo era criar um menu com 4 opções: soma, multiplicar matrizes, multiplicar listas e achar números primos


def menu ():
  x = int(input("\n1-Soma\n2-Multiplicar matrizes\n3-Multiplicação de listas\n4-Numeros primos\n0-Sair\nDigite:"))

  if x == 1:
    print(soma())
  elif x == 2:
    mult()
  elif x == 3:
    mlist()
  elif x == 4:
    a = int(input("Digite um numero (de 3 a 81): "))
    prim(a,2)
  elif x == 0:
    print("Saindo...")
  else:
    print("Não disponível")
  return x

def soma():
  a = int(input("Digite um numero:"))
  b = int(input("Digite outro numero:"))
  s = a + b

  return s

def mult():
  #a saída tá saindo bugada, mas tá quase certo D:
  a = int(input("Digite a quantidade de colunas da matriz R:"))
  b = int(input("Digite a quantidade de linhas da matriz R:"))

  matriz1 = []
  matriz2 = []

  for i in range(b):
    coluna = [0] * a
    matriz1.append(coluna)
  for i in range(b):
    for j in range(a):
      matriz1[i][j] = int(input("matriz1[{}][{}] = ".format(i + 1, j + 1)))
  for i in matriz1:
    print(i)

  for i in range(b):
    coluna = [0] * a
    matriz2.append(coluna)
  for i in range(b):
    for j in range(a):
      matriz2[i][j] = int(input("matriz2[{}][{}] = ".format(i + 1, j + 1)))
  for i in matriz2:
    print(i)

  def multimatriz(matriz1, matriz2):
    MRlinhas = len(matriz1)
    MRcolunas = len(matriz1[0])
    MR = []
    for i in range(MRlinhas):
      MR.append([])
      for j in range(MRcolunas):
        val = 0
        for k in range(len(matriz2)):
          val += matriz1[i][k] * matriz2[k][j]
          MR[i].append(val)
    return MR

  for i in multimatriz(matriz1, matriz2):
    print(i)

def mlist():
  lista = []
  listaR = []
  print("\n")
  for i in range(10):
    lista.append(int(input("Digite:")))
    listaR.append(lista[i]*5)
  print(lista)
  print(listaR)

primos=[2,3]
def prim(a,b):
  if a==3:
    return print(sorted(primos))
  if (a-b) > 1:
    if a % (a-b) !=0:
      return prim(a, b+2)
    else:
      return prim(a-1, 2)
  elif (a-b) == 1:
    primos.append(a)
    return prim(a-2, 2)


while 1:
  menu()
  if menu() == 0:
    break
