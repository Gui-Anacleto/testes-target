#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.


#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

with open("dados.json", encoding='utf-8') as meu_json:
   dados = json.load(meu_json)

for i in dados:
   x=i['valor']

print("TOTAL: ",x)
#   if x != 0:

#      print(x)








    
    
    
        