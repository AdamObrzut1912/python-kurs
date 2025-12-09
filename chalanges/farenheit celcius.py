def cTof(celcius):
    farenheit = celcius * 9 / 5 + 32
    print(f"{celcius} stopni celcjusza to {farenheit} stopnii faranheita")
    return farenheit

def fToC(farenheit):
    celcius = (farenheit-32) * 5 / 9
    print(f"{farenheit} stopni farenheita to {celcius} stopnii celcjusza")
    return celcius

cTof(20)
fToC(86)
