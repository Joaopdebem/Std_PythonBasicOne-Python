nome = str(input("Digite seu nome completo: ").lower().strip())

print("Olá, {}.".format(nome.capitalize()))
print("Seu primeiro nome é {}.".format(nome.split()[0].capitalize()))
print("Seu último nome é {}.".format(nome.split().pop().capitalize()))