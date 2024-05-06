salario_cidadao = []
filhos_cidadao = []
salarios_menor = []
media_salario = 0
media_filhos = 0


print("Pesquisa Prefeitura")
salario = float(input("Informe seu salario: "))
salario_cidadao.append(salario)
media_salario = media_salario + salario
filho = int(input("Quantos filhos tem: "))
filhos_cidadao.append(filho)
print()
adcionar_habitantes = input("Deseja adicionar mais um habitante: ")
while (adcionar_habitantes == "sim"):
    print("Pesquisa Prefeitura")
    salario = float(input("Informe seu salario: "))
    salario_cidadao.append(salario)
    media_salario = media_salario + salario
    filho = int(input("Quantos filhos tem: "))
    filhos_cidadao.append(filho)
    media_filhos = media_filhos + filho
    print()
    adcionar_habitantes = input("Deseja adicionar mais um habitante")
else:
    print("Coletado todos os dados!")

















