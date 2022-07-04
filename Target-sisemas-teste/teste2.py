numero = int(input("Que termo deseja encontrar: "))
n1=0
n2=1
n3=0

while numero > n3:
    n3 = n1+n2
    n1 = n2
    n2 = n3

if  numero == 0:
    print("Esta na seguencia de Fibonacci")

elif numero == n3:
    print("O numero {} está na sequencia de Fibonacci".format(numero))

else:
    print("Este numero não pertence sequencia de Fibonacci")



