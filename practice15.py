class the_holy_trinity:
    def __init__(self,brand,model,top_speed):
        self.brand=brand
        self.model=model
        self.topspeed=top_speed

    def info(self):       
        return f'The car we are looking at is a {self.brand}\nIts a {self.model} and it can clock upto {self.topspeed}'
    
ferrari=the_holy_trinity("Ferrari","la ferrari","250 miles per hour")
print(ferrari.info())
porsche=the_holy_trinity("Porsche","Porsche 918 spyder","250 miles per hour")
print(porsche.info())        
Mcleran=the_holy_trinity("Mcleren","Mcleren P1","250 miles per hour")
print(Mcleran.info()) 

ferrari2=the_holy_trinity("Ferrari","488 pista","220 miles per hour")
print("This is not a part of the holy trinity but its a beast")
print(ferrari2.info())