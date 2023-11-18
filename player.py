class Player:
    def __init__(self,name,age,rank):
        self.name = name
        self.age = age
        self.rank = rank
    def information(self):
        print("the palyer name{}the age{}rank{}:" ,format(self.name, self.age, self.rank))
player1 = Player("sara",23,54)
player1.information()