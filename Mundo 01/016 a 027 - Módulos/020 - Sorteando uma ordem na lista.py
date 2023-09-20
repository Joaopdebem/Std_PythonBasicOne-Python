import random

aluno1 = input("Primeiro nome: ")
aluno2 = input("Segundo nome: ")
aluno3 = input("Terceiro nome: ") 
aluno4 = input("Quarto nome: ")

alunos = list([aluno1, aluno2, aluno3, aluno4])
apresentacao = random.sample(alunos, k=4)

print("O primeiro apresentar será {}, o segundo {}, o terceiro {} e o último {}.".format(apresentacao[0], apresentacao[1], apresentacao[2], apresentacao[3]))