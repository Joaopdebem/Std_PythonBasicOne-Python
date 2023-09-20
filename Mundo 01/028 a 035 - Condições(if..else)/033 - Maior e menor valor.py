numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

max = numero1
    
if numero2 > max:
    max = numero2
if numero3 > max:
    max = numero3

print("O maior número é {}.".format(max))

min = numero1

if numero2 < min:
    min = numero2
if numero3 < min:
    min = numero3
    
print("O menor número é {}.".format(min))