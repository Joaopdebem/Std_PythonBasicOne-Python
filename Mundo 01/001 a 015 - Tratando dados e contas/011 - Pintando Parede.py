larguraParede = float(input("Digite a largura da parede metros: "))
alturaParede = float(input("Digite a altura da parede em metros: "))

areaParede = alturaParede * larguraParede

print("Sua parede tem {} metros de largura, {} metros de altura, o que da uma área de {} metros quadrados. Para pintar toda sua parede você vai usar {} litros de tinta.". format(larguraParede, alturaParede, areaParede, areaParede/2))