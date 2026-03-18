import os
palavra_secreta="perfume"
letra_acertadas='' #usar str vazia
numero_tentativas=0
while True:
    letra_digitadas=input("Digite uma letra:")
    numero_tentativas+=1
    if len(letra_digitadas)>1:
        print("Digite apenas uma letra")
        continue
    if letra_digitadas in palavra_secreta:
        letra_acertadas+=letra_digitadas
    palavra_formada=''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertadas:
            palavra_formada+=letra_secreta
        else:
           palavra_formada+='*'
    print('Palavra formada:', palavra_formada)
    if palavra_formada==palavra_secreta:
        os.system('cls') #Comando limpar terminal
        print("VC ACERTOU!!PARABENS")
        print('A palavra era', palavra_secreta)
        print('Tentativas:',numero_tentativas)
        letra_acertadas='' #usar str vazia
        numero_tentativas=0