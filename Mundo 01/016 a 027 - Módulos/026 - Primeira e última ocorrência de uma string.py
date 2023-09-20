frase = str(input("Digite uma frase: ").strip().lower())

print("Você digitou {}, nessa string apareceu a letra 'a' {} vezes.".format(frase.capitalize(), frase.count('a')))
print("A primeira letra 'a' na primeira vez apareceu na posição {}.".format(frase.find('a')))  
print("A última letra 'a' apareceu na posição {}.".format(frase.rfind('a')))