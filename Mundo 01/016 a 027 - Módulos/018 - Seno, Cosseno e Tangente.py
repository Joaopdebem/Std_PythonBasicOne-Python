import math

angulo = int(input("Digite o ângulo que deseja consultar: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print("Angulo digitado foi {:.1f}º, seu seno é {:.3f}, o cosseno é {:.3f} e a tangente {:.3f}.".format(angulo, seno, cosseno, tangente))