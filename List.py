my_list = [1, 2, 3]
len(my_list)

print(type(my_list))



isim = "Ali"
mixed_list = [1, 2.3, "BilgeAdam", [1, 2, 3], None, True, isim]
print(len(mixed_list))

print(my_list[0])
print(type(mixed_list[0]))
print(type(mixed_list[3]))
type(mixed_list[5])
type(mixed_list[4])


# Alıştırma
list_in_list =[[[1, 2], [3, 4]], [[5, 6],[7,8]]]
list_in_list[1]
list_in_list[1][0][1]

# liste toplama
list1= ["apple","banana", "apple"]
list2= ["grape", "strawbery", "avocado"]

list3= list1 + list2
print(list3)

list4= [list1] + [list2]
print(list4)
print(len(list4))

fruits= ["apple", "pear", "strawberry", "orange", "apricot"]
# eleman değiştirme
fruits[3] = "watermelon"
print(fruits)

#negative indexing
fruits[-1]

#list slicing (dilimleme)

fruits[1:4]
fruits[1:4:2]
fruits[2:4] = ["cherry", "avocado"]
print(fruits)

# eleman ekleme

numbers= [0, 1, 2,3]
numbers+=[4]
print(numbers)

#eleman silme
print(numbers)
del numbers[3]
print(numbers)

print(fruits)
del fruits[2]
print(fruits)

# Aritmetik İşlemler
age= [37, 24, 25, 18, 17, 13, 24, 31, 27]
max(age)
min(age)
sum(age)
sum(age)/ len(age)  #ortalama 

import math

math.pi







