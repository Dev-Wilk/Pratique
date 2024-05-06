valor = int(input("Digite um valor "))
multiplicador = 1

if (0 < valor > 10 ):
    valor = int(input("Digite um valor diferente que esteja de 0 ate 10: "))

while  multiplicador != 11:
    print("{multiplicador} x {valor} = {resultado}".format(multiplicador = multiplicador , valor = valor, resultado = multiplicador*valor ))
    multiplicador +=1

