salario = float(input("Digite seu salário: "))

if salario <= 1250:
    print("Com o aumento seu salário passou a ser R${:.2f}.".format((salario * 0.15) + salario))
elif salario > 1250:
    print("Seu novo salario será de R${:.2f}".format((salario * 0.10) + salario))