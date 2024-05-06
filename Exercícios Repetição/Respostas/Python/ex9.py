numeros = []
media_numero = 0

quantidade_lido = int(input("Digite a quantidade de numeros que deseja ler: "))

for i in range(quantidade_lido):
    numero = int(input("digite o numero que deseja: "))
    numeros.append(numero)
    media_numero = media_numero + numero

maior_numero = max(numeros)
menor_numero = min(numeros)
media_numero =  media_numero / quantidade_lido

print()
print(maior_numero)
print()
print(menor_numero)
print()
print(media_numero)