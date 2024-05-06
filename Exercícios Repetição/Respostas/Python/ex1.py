numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite um numero: "))

while numero2 == 0 :
    print("Valor Invalido!")
    numero2 = float(input("Digite um numero: "))

 
divisao = (numero1 / numero2)

print("A divisão ficou {:.2f}".format(divisao))