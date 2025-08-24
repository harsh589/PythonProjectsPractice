class single:
    def __init__(self,Animal):
        self.Animal = Animal
    
    def display(self):
        print(f"Hello i am the {self.Animal}")

class two(single):
    def __init__(self,Animal,breed):
        super().__init__(Animal)
        self.breed = breed

    def display2(self):
        print(f"hello i am a child of {self.Animal} and it has breed {self.breed}")


p  = two("dog","german");
p.display2()