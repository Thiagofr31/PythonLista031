#Fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula prestação	=
#valor	+	(valor	x	(taxa	:	100)	x	tempo	em	dias)

dias =  float(input("Qual o tempo de atraso da sua prestação (em dias): "))
valor = float(input("Qual o valor da prestação: "))
taxa = float(input("Qual a taxa: "))

prestacao = valor + (valor * (taxa / 100) * dias)

print("O valor da prestação com atraso é:" , prestacao)









