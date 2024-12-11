class Cars:
    Company = 0
    Price = 0
    Color = 0
    def Car(self):
        print("Car company - ",self.Company)
        print("Car Price - ",self.Price)
        print("Car color - ",self.Color)
        print("\n")
car1 = Cars()
car1.Company = "Toyota"
car1.Price = "75,000,00"
car1.Color = "Golden Red"
car1.Car()

car2 = Cars()
car2.Company = "Skoda"
car2.Price = "15,000,00"
car2.Color = "Black"
car2.Car()

car3 = Cars()
car3.Company = "Volkswagen"
car3.Price = "32,000,00"
car3.Color = "Matte BLue"
car3.Car()
