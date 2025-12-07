experience = 2
languages = ["python", "typescript", "javascript", "java"]
contractType = "b2b"

if experience >= 2 and "python" in languages and "java" in languages:
    if contractType == "b2b" or contractType == "employed":
        print("kandydat został przyjęty")
    else:
        print("kandydat nie został przyjęty przez wartośc zatrudnienia")
else:
    print("kandydate nie został przyjęty")