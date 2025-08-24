class Father():
    def skill(self):
        print("I am driving the car")

class Mother():
    def skill(self):
        print("I am cooking")


class child(Mother,Father): #jo pahale hoga whi inherit karega
    def skill(self):
        super().skill()
        print("mine")

x =child()

x.skill()