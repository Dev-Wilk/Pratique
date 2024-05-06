numeros =[]
numeros_negativo=[]

for i in range(10):
    numero = int(input("Digite um numero: "))
    numeros.append(numero)
    if numero < 0 :
        numeros_negativo.append(numero)


print(numeros_negativo)