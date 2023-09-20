print("Informe o comprimento de 3 retas para saber se forma um triângulo ou não.")

reta1 = int(input("Digite a primeira reta em metros: "))
reta2 = int(input("Digite a segunda reta em metros: "))
reta3 = int(input("Digite a terceira reta em metros: "))

if (reta1 + reta2 == reta3) or (reta1 + reta3 == reta2) or (reta2 + reta3 == reta1):
    print("Tringulo")
else:
    print("Nao triangulo")

    