diasAlugado = int(input("Quantos dias você ficou com o carro? "))
kmPercorrido = float(input("Digite em quantidade de KM percorridos: "))

diasCobrados = diasAlugado * 60
kmCobrados = kmPercorrido * 0.15

totalCobrado = diasCobrados + kmCobrados

print("Foi cobrado R${:.2f} reais pelos {} dias alugados, R${:.2f} reais pelos {:.1f} quilometros percorridos, com isso fechamos sua conta em R${:.2f} reais. ".format(diasCobrados, diasAlugado, kmCobrados, kmPercorrido, totalCobrado))