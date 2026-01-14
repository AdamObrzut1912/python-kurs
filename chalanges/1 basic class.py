class Pizza:
    def __init__(self):
        self.ingredients = []

    def addIngredients(self, ingredient):
        if isinstance(ingredient, str) == True:
            self.ingredients.append(ingredient)

    def showIngredients(self):
        for i in self.ingredients:
            print(i)
    

polskaPizza = Pizza()
polskaPizza.addIngredients("pieczarki")
polskaPizza.addIngredients("ser",)
polskaPizza.addIngredients("pomidor")
polskaPizza.showIngredients()