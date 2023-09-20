dinheiro = input("Digite quanto dinheiro você tem na carteira: ")

print("Certo então, você possui {} reais, com isso você pode comprar {} dolares com base na cotação atual.".format(dinheiro, round(float(dinheiro)/5.16,2)))