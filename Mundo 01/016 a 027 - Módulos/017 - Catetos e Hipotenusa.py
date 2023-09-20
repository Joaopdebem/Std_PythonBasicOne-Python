import math

cateto1 = float(input('Digite o comprimento do cateto oposto: '))
cateto2 = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(cateto1, cateto2)

print("Com o cateto oposto sendo {:.2f} e o adjacente {:.2f}, a hipotenusa será {:.2f}.".format(cateto1, cateto2, hipotenusa))