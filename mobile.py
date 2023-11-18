class Mobile:
    def __init__(self,companyNme,storage,serialNum,name,dualSim):
        self.companyNme = companyNme
        self.storage = storage
        self.serialNum = serialNum
        self.name = name
        self.dualSim = dualSim
    def afficher():
        print("companyNme{}storage{}serialNum{}name{}dualSim{}:"affiche(self.companyNme,
             self.storage, self.serialNum, self.name, self.dualSim))
mobile1 = Mobile("redmi","128GB","ZLOLPRO5437R","Redmi C33","yes")
mobile1.afficher()
