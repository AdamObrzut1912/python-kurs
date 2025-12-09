print("Hello " + "world")
print("Hello" * 3)

string = "hello world"

print(string[0])
print(string[0:5])

print("hello" in string)
print("hello" not in string)

multiline = """line1
line2
line3
"""

print("ala".capitalize())
print("Ola ma kota, Ola ma psa".count("Ola"))

print("Hello".center(20,"-"))

print(string.startswith("hello"))
print(string.endswith("world"))


print(string.find("Ola"))
print(string.find("world"))
print("Ola ma psa, Ola ma kota".rfind("Ola"))

print("34324234234".isalnum())
print("34324234234.".isalnum())
print("34324234234 g".isalnum())

print("34324234234 g".isalpha())
print("kot".isalpha())
print("kot ".isalpha())
print("kot2".isalpha())

print("test".islower())
print("tesT".islower())

print("TEST".isupper())

print("TEST".isspace())
print("   \n \t".isspace())


print("-|".join(["Ala", "Ola", "Adam"]))


print("Hello World".lower())
print("Hello World".upper())
print("Hello World".swapcase())


print("     \n \t Hello World \n ".lstrip())
print("     \n \t Hello World \n ".rstrip())
print("     \n \t Hello          World \n ".strip())

print("Ola ma psa, Ola ma kota".replace("Ola", "Kasia"))


print("My name is {myName}, I'm from {country}".format(myName = "Kuba", country = "Poland"))
print("My name is {myName}, my postal code is {code}".format(myName = "Kuba", code = "11789"))
print("My name is {0}, my postal code is {1}".format("Kuba", 11789))
print("My name is {}, my postal code is {}".format("Kuba", 11789))