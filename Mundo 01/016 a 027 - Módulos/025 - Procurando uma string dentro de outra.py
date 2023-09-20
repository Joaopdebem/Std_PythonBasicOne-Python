nome = str(input("Qual o seu nome? ")).strip()
nomeTratado = nome.lower().split()

if 'silva' in nomeTratado:
    print("Você se chama {}, que legal você possui Silva no nome.".format(nome.capitalize()))
else:
    print("Seu nome é: {} Você não tem Silva no nome.".format(nome.capitalize()))