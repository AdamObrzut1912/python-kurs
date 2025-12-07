raining = False
haveUmbrella = False
temperature = 14

if temperature >= 40 or temperature <= 0:
    print("Zostańw w domu")
elif temperature > 0 and temperature < 10 and haveUmbrella == True and raining == True:
    print("możesz wyjśc z parasolka")
elif raining == False and temperature >= 10:
    print("możesz wyjść bez parasolki")
else:
    print("zostań w domu")