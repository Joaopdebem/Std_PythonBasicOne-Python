precoProduto = float(input("Digite um preço de um produto: R$"))
descontoProduto = float(precoProduto)*0.05

print("O preço do produto é: R${} reais. Ele com 5% de desconto sai por: R${} reais.".format(precoProduto, precoProduto-descontoProduto))