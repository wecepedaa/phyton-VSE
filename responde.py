from random import randrange

valor = randrange(10)
print(f"El valor: {valor} \n")
for i in range(valor):
  i += valor
  print(i)
