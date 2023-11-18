class Car:
    def __init__(self,speed,enginePower,color,name):
        self.speed = speed
        self.enginePower = enginePower 
        self.color = color 
        self.name = name 
    def afficher(self):
        print("speed{}enginePower{}color{}name{};"affiche(self.speed, self.enginePower,
              self.color, self.name))
car1 = Car(160,"yes","black","JAC")
car1.afficher()