"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda',(0,10,20,30,40) ],  # 2
]

print(salas[2][2])   #COMEÇA LISTA E DEPOIS O INDICE
print(salas[2][3][3]) #lista, indice lista, indice 
for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)