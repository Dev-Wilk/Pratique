numeros =[]

for i in range(10):
    numero = int(input("Digite um numero: "))
    numeros.append(numero)

numeros_pares = [numero for numero in numeros if numero % 2 == 0]
print("Numeros pares: ", numeros_pares)