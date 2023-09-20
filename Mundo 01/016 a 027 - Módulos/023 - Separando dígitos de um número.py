numero = int(input("Digite um número de 0 a 9999: "))
unidade = numero // 1 % 10
dezena = numero //10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print("O número digitado foi {}.".format(numero))
print("E a unidade {}.".format(unidade))
print("A dezena {}.".format(dezena))
print("A centena é {}.".format(centena))
print("O milhar do número é {}.".format(milhar))