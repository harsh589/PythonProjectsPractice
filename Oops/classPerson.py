class Person: #class h ye
    def __init__(self, name, age): 
        self.name = name
        self.age = age


#show function is not neccessary
    def show(self):
        print(f"Hello my name is {self.name} and age is {self.age}")

s1 = Person("harsh", 33) # object hai ye
s1.show()
