#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:

#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json
import operator

with open("dados.json", encoding='utf-8') as meu_json:
   dados = json.load(meu_json)

min=0
max=0
contaDia = 0
soma=0
contaDiaMedia = 0

#print("=====LISTA COMPLETA=====")
for i in dados:
   if i['valor'] != 0:
      #print(i)
      x=i['valor']
     
      contaDia += 1
      soma = x + soma
      media = soma/contaDia
   
      if max < i['valor']:
         max = i['valor']
         maxDia=i['dia']

      min = max
      if min > i['valor']:
         min = i['valor']
         minDia=i['dia']

      if i['valor'] >= media:
         diaNaMedia = i['dia']
         contaDiaMedia += 1 

print("=====RESULTADOS=====")
print("Menor valor: {}, encontrado no dia {}".format(min,minDia))
print("Maior valor: {}, encontrado no dia {}".format(max,maxDia))
print("Dias que ficaram na media: {} ".format(contaDiaMedia))
#print("TOTAL: ",soma)
#print("Media: ",media)
#print("Dias com valor diferente de 0: ",contaDia)








    
    
    
        