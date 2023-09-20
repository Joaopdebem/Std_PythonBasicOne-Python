print("Vamos verificar se você foi multado ou não.")

velocidadeCarro = float(input("Digite a velocidade que seu carro estava: "))
multa = (velocidadeCarro - 80) * 7

if velocidadeCarro <= 80:
    print("Você estava a {:.1f}Km/h, dentro do permitido, não foi multado.".format(velocidadeCarro))
elif velocidadeCarro > 80:
    print("Você ultrapassou o limite de velocidade, você estava a {:.1f}Km/h, você foi multado em R${:.1f}.".format(velocidadeCarro, multa))
    
    