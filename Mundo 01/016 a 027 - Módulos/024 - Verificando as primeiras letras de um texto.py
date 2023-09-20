cidade = str(input("Onde você mora? ")).strip()
cidadeTratada = cidade.lower().split()

if cidadeTratada[0]== 'santo':
    print("Você mora em {}, que legal sua cidade começa com Santo.".format(cidade.capitalize()))
else:
    print("Sua cidade se chama {}.".format(cidade.capitalize()))