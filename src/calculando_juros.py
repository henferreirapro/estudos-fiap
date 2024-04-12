linha = "=" * 92

print(f"{linha}\n")
# Verificando o valor da divida
while True:
  valor_divida = input("  Por favor Digite o valor da divida sem pontos e virgulas, apenas números. \n  Valor: ")

  # verificando se é um valor inteiro.
  if valor_divida.isdigit():
    valor_divida = int(valor_divida)
    print(f"\n{linha}\n")
    break
  else:
    print(f"\n  Dado Invalido!! Por favor, tente novamente. \n{linha}\n")


# Verificando os valores e mostrando o resultado 
juros = 0
parcelas = 1
calculo_juros = 0

print(f"  Resultado\n{linha}")

for i in range(5):

  if i <= 0:
    parcelas = 0
    valor_divida_juros = valor_divida
    juros = 0.05
    valor_parcelas = valor_divida
    
  else:
    parcelas += 3
    juros += 0.05
    calculo_juros = valor_divida * juros
    valor_divida_juros = valor_divida + calculo_juros
    valor_parcelas = valor_divida_juros / parcelas


  # Visualização em tabela vertical
  # print(f" Total: R$ {valor_divida_juros:.2f}\n Juros: R$ {calculo_juros:.2f}\n Numero de parcelas: {parcelas}\n Valor da Parcela: R$ {valor_parcelas:.2f}.\n{linha}")

  # Visualização em tabela horizontal(Igual a do exemplo)
  print(f"  Total: R$ {valor_divida_juros:.2f}  Juros: R$ {calculo_juros:.2f}  Numero de parcelas: {parcelas}  Valor da Parcela: R$ {valor_parcelas:.2f}.")

print(f"\n{linha}")