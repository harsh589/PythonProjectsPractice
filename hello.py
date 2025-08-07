print("hello")
x = 4
y = 5

if x > y:
    print("x bada hai")
elif y > x:
    print("y bada hai")


def sum():
    print("do number ka sum")
sum()

def multiply(a,b):
    print(a*b);

multiply(33,13)


list = ["harsh","matku","madhu"]
print(len(list))
print(list[2])

print(list.append("motu"))
print(list)

for x in list:
    print(x);



#print 2 table

for x in range(1,20):
    if(x%2==0):
        print(x);


##name = input("enter name")
#age = int(input("enter age"))

#if(age>18):
 #   print("eligible for ai course")
#else:
 #   print("thodaaa seekh le bhai")


def add(a,b):
    return a+b

print(add(44,23))


def is_Eligible(age):
    if(age>18):
      return "tu hai whi"
    else:
     return "tu nhi hai"


print(is_Eligible(33))


def square_all(numbers):
    return [i * i for i in numbers]

print(square_all([4, 5, 2, 11, 33]))
