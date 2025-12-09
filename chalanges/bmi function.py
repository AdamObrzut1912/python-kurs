def calculateBMI(waga, wzrost):
    bmi = waga / ((wzrost / 100) ** 2)
    print(bmi)
    return bmi


def classifyBMI(bmi):
    if bmi < 18.5:
        print("masz niedowagę")
    elif(bmi < 25):
        print("Twoja waga jest w normie")
    elif bmi < 30:
        print("masz nadwagę")
    else:
        print("masz sporą niedowagę")

wagaUżytkownika = int(input("Podaj swoją wagę"))
wysokoscUżytkownika = int(input("Podaj swój wzrost"))

bmiUzytkownika = calculateBMI(wagaUżytkownika, wysokoscUżytkownika)

bmiUzytkownika

classifyBMI(bmiUzytkownika)

