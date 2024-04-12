linha = "=" * 90

print(f"""
{linha}
    Bem Vindo ao Simulador de calculo da compra do seu veiculo""")

# Pegando o valor do veiculo
while True:
  valor_veiculo = (input("    Digite o valor do veiculo sem virgulas ou pontos. \n    Valor do Veiculo: "))

  # verificando se o valor é um valor int.
  if valor_veiculo.isdigit():
    valor_veiculo = int(valor_veiculo)
    print(f"{linha}\n")
    break
  else:
    print(f"""\n  Dados invalidos!!! \n  Por favor digite os valores corretos.
{linha}
""")


# Calculando valor com 20% desconto
valor_desconto_20 = valor_veiculo - (valor_veiculo * 0.2)
print(f"  O preço final do veiculo a vista com desconto de 20% é R$ {valor_desconto_20:.2f}.")


# Calculando os valores com Juros
juros = 0
valor_parcela = 0

for i in range(10):

  # O round() serve para definir as casas decimais após a virgula
  juros = round(juros + 0.03, 2)
  valor_parcela = valor_parcela + 6
  valor_total_veiculo_juros = valor_veiculo + (valor_veiculo * juros)


  print(f"  O preço final do veiculo parcelado em {valor_parcela}x é R$ {valor_total_veiculo_juros:.2f}, com parcelas de R$ {valor_total_veiculo_juros / valor_parcela:.2f}.")


print(f"\n{linha}")