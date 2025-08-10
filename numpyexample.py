import numpy as np


arr = np.array([2,3312,2])
print(arr)


arr2 = np.array([[1,2,3],[4,5,6]])

print(arr2)
print(type(arr2))
print(type(arr))

arr3= np.array([1,2,3,4,5,6])

print(arr3[2])
print(arr3[1:3 ])


arr4 = np.array([1, 2, 3, 4], dtype='S')

print(arr4)
print(arr4.dtype)

#copy vs view


arr5 = ([3,4,5,6,7])

copy_arr5 = arr5.copy()

arr5[0] = 100

print(arr5)

#copy wale mai change nahi hoga


#view mai chnage ho jayega sab jagah
arr2 = np.array([10, 20, 30, 40])
view_arr = arr2.view()

arr2[1] = 777

print("Original:", arr2)      # [10 777 30 40]
print("View:    ", view_arr)  # [10 777 30 40]




#shape
arr6 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr6.shape)


arr7 = np.array([1,2,3,4,5,6,7,8,9,10])

print(arr7.reshape(2,5))


#iteration using nditer()

for x in np.nditer(arr7):
    print(x)

#when i want to change the datatype from one other then we use op_dtype


for z in np.nditer(arr7,flags=['buffered'],op_dtypes=['S']):
    print(z)


    for a in np.nditer(arr7,flags=["external_loop"]):
        print(a)