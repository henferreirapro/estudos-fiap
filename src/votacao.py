# Listas
dias_semana = [
  "Segunda-Feira", "Terça-Feira", "Quarta-Feira", 
  "Quinta-Feira", "Sexta-Feira"
]

dias_escolhidos = []


# Verificando a QTD de colaboradores
while True:
  qtd_colaboradores = input("""
========================================================================
  Bem vindo a votação para o melhor dia para a nossa Live.
  Quantos Colaboradores irão participar dessa votação?
  Digite apenas números: """)

  # Verificando se o que foi digitado é um valor inteiro com o .isdigit()
  if qtd_colaboradores.isdigit():
    qtd_colaboradores = int(qtd_colaboradores)
    break
  else:
    print("Dado invalido!!! \nPor favor digite um número.")
    

# Votação
for i in range(qtd_colaboradores):

  while True:
    escolha_colaborador = int(input("""
  ========================================================================
    Qual dia da semana é melhor para voce participar da nossa Live?
    Escolha o número da opção desejada a baixo:
      [ 1 ] - Segunda-Feira
      [ 2 ] - Terça-Feira
      [ 3 ] - Quarta-Feira
      [ 4 ] - Quinta-Feira
      [ 5 ] - Sexta-Feira
      Digite a opção escolhida: """))
    
  # verificando se o número não é maior que as opções acima.
    if escolha_colaborador >=1 and escolha_colaborador <= 5:
      dias_escolhidos.append(dias_semana[escolha_colaborador - 1])
      break
    else:
      print("\n  Opção Invalida!!! \n  Por favor digite uma opção valida.")
      

# RESULTADO
print("""
========================================================================
  Resultado da Votação:""")

for i in range(qtd_colaboradores):
  print(f"    O {i + 1}º Colaborador escolheu {dias_escolhidos[i]} como melhor dia para a Live.")