import math
import random
distance = random.randint(100,1000)
spalanie = math.ceil(distance*0.07)
cena = round(random.uniform(4.5,5.5),2)

koszt = spalanie * cena

print(koszt)

if koszt > 400:
    print("wysokie koszty")
else:
    print("przystępne ceny")