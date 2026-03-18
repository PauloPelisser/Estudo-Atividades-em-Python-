def cotacao(dolar, conversao=5.10):
    real = dolar * conversao
    return real

valores=[]
while True:
    n = float(input("Digite o valor em dólar: "))
    convertido = cotacao(n)
    valores.append(convertido)

    print(f"Valor convertido: R${convertido:.2f}")

    print("\n1 - Continuar\n0 - Parar")
    escolha = int(input("Escolha uma opção: "))
    if escolha == 0:
        break
print("\nValores convertidos:")
for v in valores:
    print(f"R${v:.2f}")
