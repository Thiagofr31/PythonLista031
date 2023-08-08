#Fazer um algoritmo que pergunte 1 número e apresente:
#a) O próprio número
#b) O quadrado deste número
#c) A raiz quadrada deste número
import math

numero = int(input("Escolha um número: "))

quadrado = numero * numero

raiz = math.sqrt(numero)

print("O número que você escolheu: " ,numero)
print("O quadrado do seu número é:" , quadrado)
print("A raiz quadrada do seu número é:" , raiz)



