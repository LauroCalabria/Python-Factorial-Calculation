#Programa pra calcular o fatorial.
n=int(input('Digite um número inteiro para calcular o seu fatorial: '))
f=1
c=n
while c>0:
    f *= c
    c -= 1
print('O fatorial de {} é igual a {}.'.format(n,f))
