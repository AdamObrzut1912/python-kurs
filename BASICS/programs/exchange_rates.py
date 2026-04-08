import requests

base = "PLN"

response = requests.get("https://cdn.kurs-walut.info/api/ecb.json")

if response.ok == True:

    
    data = response.json()
    data["base"] = base
    rates = data["rates"]
    base = data["base"]
    date = data["putISODate"]

    print("base:" + base)
    print("date:" + date)

    # print(rates)

    for key in rates:
        print(key + ": ", rates[key])