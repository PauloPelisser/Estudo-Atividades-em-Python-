#frase=' era uma vez dois lobos que eram lobos famintos'\
#'esses lobos eram brancos'\
#'esses lobos morreram'

#print(frase.count('lobo')) #Função .count é para contar quantas vezes a palavra ou numero apareceu

frase="O Python é uma linguagem de programação"\
"multiparadigma."\
"Python foi criado por Guido van Rossum."

    #Os colchetes servem para criar listas podem ser int,str,etc...

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase): # esse len seria numero de letras 
    letra_atual = frase[i]

    if letra_atual == ' ':  # tirar o espaço do contador 
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)