# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    total=1
    for numero in args:
        total*=numero
        return total
multiplicaçao=multiplicar(1,2,3,4)
print(multiplicaçao)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numeros):
    multiplo_de_dois=numeros %2 ==0
    if multiplo_de_dois:
            return f'{numeros} é par '
    else:
         return f'{numeros} é impar'
print(par_impar(2))
print(par_impar(3))
print(par_impar(4))
print(par_impar(26))
         
         
"""
Higher Order Functions
Funções de primeira classe
"""


def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)