class GrandFather:
    def buddha(self):
        print("Hello, I am buddha")

class Parents(GrandFather):
    def baapu(self):
        print("I am baap")

class Myself(Parents):
    def mine(self):
        print("Ye mai hu bidu")

# object banate hai
x = Myself()

# methods call
x.buddha()   # GrandFather ka method
x.baapu()    # Parents ka method
x.mine()     # Myself ka method
