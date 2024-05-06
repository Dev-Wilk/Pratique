numero = int(input("Digite um numeros: "))
range = 1
soma = numero

while range < 10:
    numero = int(input("Digite um numero: "))
    soma = soma + numero
    range = range + 1

soma = soma / 10
print("A media foi: {media}".format(media = soma))