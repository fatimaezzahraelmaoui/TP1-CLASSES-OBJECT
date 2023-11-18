class car:
    def __init__(self,speed,color,nitroSpeed,module):
        self.speed = speed
        self.color = color
        self.nitroSpeed = nitroSpeed
        self.module = module
    def information(self):
        print("speed{}color{}nitroSpeed{}module{}:",format(self.speed, self.color, self.nitroSpeed,
              self.module))
    car1 = car(100,red,200,2012)
    car1.information()