#5) Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

palavra = input("Digite uma palavra: ")

def reverse(text):
    result = ""
    for i in range(len(text),0,-1):
        result += text[i-1]
    return (result)

print(reverse(palavra))