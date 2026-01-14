class SimCard:
    def __init__(self):
        self.contacts = []

    def addContact(self, name, telephone):
        if isinstance(name, str) == False: return
        if isinstance(telephone, int) == False: return

        user = {
                "name": name,
                "telephone": telephone 
            }
        self.contacts.append(user)
    
    def showContacts(self):
        for i in self.contacts:
            print(i["name"]+ " " + str(i["telephone"]))

sim = SimCard()
sim.addContact("Ola", 9762385923)
sim.addContact("Adam", 123456789)
sim.addContact(100, "numer")
sim.addContact("Kasia", "numer")
sim.showContacts()


        