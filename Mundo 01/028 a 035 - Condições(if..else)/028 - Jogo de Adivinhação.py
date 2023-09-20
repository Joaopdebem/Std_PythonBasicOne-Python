import random
import time

print("-=-" * 20)
print("Olá, você está em um jogo de adivinhação!")
print("-=-" * 20)

numeroPensado = random.randint(0, 10)
numeroDigitado = int(input("Adivinhe o número que o computador escolheu de 0 a 10: "))
print("Processando...")
time.sleep(1)

if numeroPensado == numeroDigitado:
    print("Uau, você acertou, o número pensado foi {} e você digitou {}.".format(numeroPensado, numeroDigitado))
else:
    print("Que pena, você errou! O número pensado foi {} e o seu foi {}.".format(numeroPensado, numeroDigitado))