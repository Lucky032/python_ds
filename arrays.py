import array as arr

# #defining the array
a = arr.array('d',[1.1,2.2,1.3])
print(a)

#adding the elements
a.append(2.2)
print(a)

#Extend the elements
a.extend([5.9,2.3,4.1])
print(a)

#Removing of elements
print(a.pop(1))

import array as arr
#defining the array
a = arr.array('d',[10, 20, 30, 40, 50])
print(a[0],a[2],a[4])

#Insert any element at second position of an array ex: 25
a.insert(2,25)
print(a)

