# Aula 04 - Exercício 01

# Criando uma variável para receber seu texto

msg = 'Olá mundo!'  # O texto pode ser entre aspas simples ou dupla. Vamos sempre utiliza aspas simples.

print(msg)  # Como eu criei uma variável, ela não precisará estar dentro das aspas, apenas dentro do ()



# Criando um outro exercício utilizando If, Elif e Else

var = int(input('Digite um número? '))

if var > 0:
    print(var,'é maior que Zero')
elif var == 0:
    print(var, 'é igual a Zero')
else:
    print(var, 'não é maior que Zero')
