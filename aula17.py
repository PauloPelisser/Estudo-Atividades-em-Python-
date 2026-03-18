# if / elif      / else
# se / se não se / se não

condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = True

if condicao1:   #POSSO TER UM IF SOZINHO
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:                       #NAO POSSO TER UM ELIF SOZINHO DEPENDE DO IF 
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:                                     #NAO POSSO TER UM ELSE SOZINHO DEPENDEN DO IF
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if')