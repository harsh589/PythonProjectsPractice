import numpy as np

x = np.random.randint(100)   # ✅ 0 se 99 ke beech ek random integer
print(x)

#rand use for flaott and randint use for int

y = np.random.randint(100,size=(7))
print(y)


z = np.random.choice(([3, 5, 7, 9]))
print(z)