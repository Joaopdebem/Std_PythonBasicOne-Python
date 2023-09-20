nome = input("Digite seu nome: ")


print("Você digitou {}.".format(nome))
print("Seu nome é em letra maiúscula fica {}.".format(nome.upper()))
print("Em minúscula {}.".format(nome.lower()))
print("A quantidade de letras sem os espaços que seu nome possui é {} letras.".format(nome.replace(" ", "").__len__()))
print("Seu primeiro nome tem {} letras.".format(nome.split(" ").pop(0).__len__()))