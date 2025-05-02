mylist = [1,2,3]
mylist2 = ['bir',2,True,5.9] # python da farklı veri tipleri bir dizi içerisinde tutulabilir

list1 = ["one","two","three"]
list2 = ["four","five","six"]
 
numbers = list1 + list2 # direkt böyle toplama yapabiliyoruz ilginç
print(numbers)

print(len(numbers)) # tıpkı stringlerde olduğu gibi eleman sayısını bize verir

print(numbers[2])

userA = ["fatih",18]
userB = ["sadık",32]

users = userA + userB # bu şekilde yaparsak dizinin 4 elemanı olur
print(users)
print(len(users))

users = [userA,userB] # böyle 2 boyutlu bir dizi elde etmiş olduk

print(userA)
print(userB)
print(users)
print(len(users))

print(users[1][0])
print(users[0][1])