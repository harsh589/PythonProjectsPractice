import sys
print(sys.executable)

add = lambda a,b : a+b
print(add(44,2))


num = [4,23,2,3,2]

sq = list(map(lambda x:x*x,num))
print(sq)


num2 = [1, 2, 3, 4, 5, 6]

evem =  list(filter(lambda x: x%2==0,num2))
print(evem)


names = ["Ram", "Shyam", "Krishna", "Om"]

lengthwale = list(filter(lambda x : len(x)>4,names))
print(lengthwale)


def add(a,b):
    return a +b

print(add(5,2))