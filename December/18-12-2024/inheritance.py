class fruits:
    def eat(self):
        print("We can eat fruits")

class Orange(fruits):
    pass
    def eat(self):
        print("Orange is a sour fruits")

class Apple(fruits):
    def eat(self):
        print("Apple is a sweet fruits")
org1 = Orange()
app1 = Apple()
org1.eat()
app1.eat()
