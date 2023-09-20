print("Iremos calcular o preço de sua viagem.")

km = float(input("Digite a quantos quilometros você está do seu destino: "))

if km <= 200:
    print("O preço de sua viagem ficou R${:.1f}.".format(km * 0.5))
else:
    print("O valor de sua viagem será de R${:.1f}.".format(km * 0.45))