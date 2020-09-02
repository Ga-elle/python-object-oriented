class CoffeeMachine():

    WATER_LEVEL = 100

    # Une méthode protégée est accessible à l'intérieur d'une classe mais ne doit pas être aisément accessible de l'extérieur
    # On ajoute un underscore en début du nom
    def _start_machine(self):
        if self.WATER_LEVEL > 20:
            return True
        else:
            print("Please add water")
            return False

    # Pour les méthodes privées, on ajoute deux underscore
    def __boil_water(self):
        return "bolling..."

    def make_coffee(self):
        if self._start_machine():
            self.WATER_LEVEL -= 20
            print(self.__boil_water())
            print("Coffee is ready!")

machine = CoffeeMachine()
for i in range(0,5):
    machine.make_coffee()

# Je peux quand même exécuter une méthode privée hors de ma classe
print("Boil water: private", machine._CoffeeMachine__boil_water())
