peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

IMC = peso / (altura ** 2)

if IMC > 25:
    print("Acima do peso")
else:
    print("Peso normal")