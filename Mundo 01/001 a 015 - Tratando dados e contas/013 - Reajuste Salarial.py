salarioAtual = float(input("Digite sua atual salário: R$"))
aumentoSalario = float(salarioAtual)*0.05
salarioNovo = float(salarioAtual) + float(aumentoSalario)

print("Seu salário atual é: R${:.2f} reais. Com o seu aumento de 15% irá ficar R${:.2f} reais.".format(salarioAtual, salarioNovo))