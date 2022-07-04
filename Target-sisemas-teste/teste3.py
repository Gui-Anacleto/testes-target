#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.


#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

with open("dados.json") as f:
   obj_pyhton = json.load(f)

print(obj_pyhton[0]['dia'])
print(obj_pyhton[0]['valor'])

print(obj_pyhton[0].values())







    
    
    
        