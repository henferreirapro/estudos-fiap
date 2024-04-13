linha = "=" * 82


# mensagem inicial
print(f"{linha}\n  Resgaste de Investimento\n{linha}")

# verificando se o valor do investimento é inteiro.
while True:
  verificando_tipo_investimento = input("  Por favor insirá apenas o número do investimento que deseja resgatar:\n  [ 1 ] - para CDB. \n  [ 2 ] - para LCI. \n  [ 3 ] - para LCA.\n  Qual das 3 opções acima? ")

  if verificando_tipo_investimento.isdigit():
    verificando_tipo_investimento = int(verificando_tipo_investimento)

    if verificando_tipo_investimento >= 1 and verificando_tipo_investimento <= 3:
      print(f"{linha}")
      break

    else:
      print(f"\n  Valor digitado INVALIDO!!! \n  Por favor, tente novamente.\n{linha}\n")
      

# vericando se o valor a ser resgatado é inteiro
while True:
  verificando_valor_resgaste = input("  Agora insira o valor a ser resgatado.\n  Digite apenas números, sem virgulas ou pontos.\n  Valor de resgate: ")
  if verificando_valor_resgaste.isdigit():
    verificando_valor_resgaste = int(verificando_valor_resgaste)
    print(f"{linha}")
    break

  else:
    print(f"\n  Valor digitado INVALIDO!!! \n  Por favor, tente novamente.\n{linha}\n")


# vericando se os dias investidos são inteiro
while True:
  verificando_dias_investidos = input("  Insira os dias que o valor ficou investido.\n  Digite apenas números, sem virgulas ou pontos.\n  Dias investidos: ")
  if verificando_dias_investidos.isdigit():
    verificando_dias_investidos = int(verificando_dias_investidos)
    print(f"{linha}")
    break

  else:
    print(f"\n  Valor digitado INVALIDO!!! \n  Por favor, tente novamente.\n{linha}\n")


# Verificando qual tipo de investimento
taxa_imposto_renda = 0

if verificando_tipo_investimento == 1:
  
  # Calculando os valores de IR para investimento CDB
  if verificando_dias_investidos <= 180:
    valor_resgatado_imposto = verificando_valor_resgaste - (verificando_valor_resgaste * 0.225)
    taxa_imposto_renda = 22.5

  elif verificando_dias_investidos >= 181 and verificando_dias_investidos <= 360:
    valor_resgatado_imposto = verificando_valor_resgaste - (verificando_valor_resgaste * 0.20)
    taxa_imposto_renda = 20

  elif verificando_dias_investidos >= 361 and verificando_dias_investidos <= 720:
    valor_resgatado_imposto = verificando_valor_resgaste - (verificando_valor_resgaste * 0.175)
    taxa_imposto_renda = 17.5

  elif verificando_dias_investidos > 720:
    valor_resgatado_imposto = verificando_valor_resgaste - (verificando_valor_resgaste * 0.15)
    taxa_imposto_renda = 15

else:
  valor_resgatado_imposto = verificando_valor_resgaste

# Mensagem de resultado com os valores de resgate
print(f" O valor resgatado do seu investimento é R$ {valor_resgatado_imposto:.2f}.\n Taxa de IR: {taxa_imposto_renda:.1f}%.\n Tempo do valor investido: {verificando_dias_investidos} dias.\n\n Lembrando que LCI's e LCA's não tem cobrança no imposto de renda, apenas CDB's.\n{linha} ")

