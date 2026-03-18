linhas=int(input("digite quantas linhas deseja adicionar:"))
colunas=int(input("digite quantas colunas deseja adicionar:"))
matriz=[]
for i in range (linhas):
    linha=[]
    for j in range(colunas):
        valor=int(input(f"Digite o valor para possição[{i}][{j}]:"))
        linha.append(valor)
    matriz.append(linha)
for linha in matriz:
    for elementos in linha:
        print(f"{elementos:5}", end=" ")
    print()