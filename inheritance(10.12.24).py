class Fruits:
    def __init__(self):
        self.Fruit1 = input()
        self.Fruit2 = input()
    def display_Fruit(self):
        print(f"Fruit 1:{self.Fruit1}\nFruit:{self.Fruit2}")

class Icecreams:
    def __init__(self):
        self.Icecream1 = input()
        self.Icecream2 = input()
    
    def display_Icecream(self):
        print(f"Icecream :{self.Icecream1}\nIcecream:{self.Icecream2}")

class Milkshake(Fruits,Icecreams):
    def __init__(self):
        Fruits().__init__(self)
        Icecreams().__init__(self)
    def display_Milkshake(self):
        self.display_Fruits()
        self.display_Icereams()

m = Milkshake()
m.display_Milkshake()

    
    
        
