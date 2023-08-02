#Fazer um programa que pergunte uma temperatura ao usuário, em graus Fahrenheit, e apresente esta
#temperatura convertida em graus Celsius. A fórmula da conversão é c	=	(f	–	32)	x	5	:	9	, onde c é a temperatura
#em graus Celsius e f em Fahrenheit

fahrenheit = int(input("Qual temperatura Fahrenheit você gostaria de saber em Celsius: " ))

celsius = fahrenheit - 32

celsius2 = celsius * 5

celsius3 = celsius2 / 9

print("Fica: " , celsius3)




