"""Escreva um programa que contenha uma função que calcule o fatorial de um número inteiro, a função aceita como argumento o numero inteiro e retorna o valor do seu fatorial."""

def fatorial(n:int, show = False):
    f = 1
    for i in range(n,0,-1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end=" ")
            else:
                print(' = ', end=" ")
        f *= i
    return f
    
numero = int(input('Informe o numero: '))
print(fatorial(numero, show = True))
