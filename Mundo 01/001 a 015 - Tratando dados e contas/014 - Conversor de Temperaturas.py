temperaturaC = float(input("Informe a temperatura em Celsius: "))
temperaturaF = (temperaturaC * 1.8) + 32
temperaturaK = temperaturaC + 273.15

print("A temperatura em Celsius está: {}ºC, convertendo isso para Fahrenheit fica {:.1f}ºF e em Kelvin {}ºK.".format(temperaturaC, temperaturaF, temperaturaK))