""" Calculadora com while """
#while True:
    #print('nummmmm')
    #########
    #sair = input('Quer sair? [s]im: ').lower().startswith('s')
    #.lower deixa tudo em minusculo a respost 
    #.startswith seria começa com: ai seria a atribuição que  vc deu 

#CALCULADORA
while True:
    numero_dig1=input("Digite um numero:")
    numero_dig2=input("Digite outro numero:")
    operador=input("Escolha um dos operadores (+,-,*,/):")
    numero_validos=None
    numero_floot1=0
    numero_floot2=0   #DEFINIR VARIAVEIS FORA DOS BLOCOD(try)
    try:
        numero_floot1=float(numero_dig1)
        numero_floot2=float(numero_dig2)
        numero_validos=True
    except: # Estamos criando linhas de erros caso digite algo errado
        numero_validos=None
    if numero_validos is None: # não sao validos, o is sign 'é'
            print("Um dos numeros são invalidos")
            continue
    
    operador_permitidos='+-/*'
    if len(operador)>1:
         print("Escolha apenas 1 sinal")
         continue
    if operador  not  in operador_permitidos: # Não está entra 
         print(" Opção invalido")
         continue
    print(" Realizando sua conta....... confira a resposta:")
    if operador=="+":
         print(f'{numero_floot1}+ {numero_floot2}=',numero_floot1+ numero_floot2)
    elif operador=="-":
         print(  f'{numero_floot1} - {numero_floot2}=',numero_floot1 - numero_floot2)
    elif operador=="*":
         print(f'{numero_floot1}* {numero_floot2}=',numero_floot1 * numero_floot2)
    elif operador=="/":
         print(f'{numero_floot1}/ {numero_floot2}=',numero_floot1 / numero_floot2)
    sair=input(" Quer sair da calculadora?[s]im:").lower().startswith('s')
    if sair is True:
         print("Saindo")
    break
