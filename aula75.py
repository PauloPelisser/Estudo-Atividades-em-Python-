# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

#FEITO POR MIM 
def duplica(numero):
    return numero *2
def triplica(numero):
    return numero *3
def quadriplica(numero):
    return numero *4

numero=5
print(f'{numero} duplicado dá {duplica(numero)} ')
print(f'{numero} triplicado dá {triplica(numero)} ')
print(f'{numero} quadriplicado dá {quadriplica(numero)} ')


#FEITO PELO PROFESSOR 
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))


