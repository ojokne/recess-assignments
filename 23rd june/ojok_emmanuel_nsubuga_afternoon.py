# OJOK EMMANUEL NSUBUGA
# REG NO: 21/U/06816/PS
# STUDENT NO: 2100706816

# LIST
# 1. Create a list of names and print the second item in the list.
 
names = ["Ojok", "Emmanuel", "Nsubuga", "Brian", "Innocent"]
print(names[1])

#2
names[0] = "Nicole"
print(names)

#3 
names.append("Peter")
print(names)

#4 
names.insert(2, "Peter")
print(names)

#5
del names[3]
print(names)

#6
print(names[-1])

#7
items = [27, 56, 12, 90, 72, 18, 99]
print(items[2:5])

#8
countries = ["Uganda", "Kenya", "Tanzania", "Burundi", "Sudan"]
countriesCopy = countries.copy()
print(countriesCopy)

#9
for country in countries:
    print(country)

#10
animals = ["dear", "monkey", "cat", "horse", "pig"]
ascendingOrder = sorted(animals)
descendingOrder = sorted(animals, reverse=True)
print("Ascending Order:", ascendingOrder)
print("Descending Order:", descendingOrder)

#11
for animal in animals:
    if 'a' in animal.lower():
        print(animal)

#12
firstNames = ["Ojok", "Opio", "Okello"]
secondNames = ["Emmanuel", "Daniel", "Innocent"]
fullNames = [first + " " + second for first, second in zip(firstNames, secondNames)]
print(fullNames)


# TUPLES
#1
x = ("samsung", "iphone", "tecno", "redmi")
fav = x[0]
print(fav)

#2
print(x[-2])

#3
x = list(x)
x[1] = "itel"
x = tuple(x)
print(x)

#4
x = x + ("Huawei",)
print(x)

#5
for phone in x:
    print(phone)

#6
x = x[1:]
print(x)

#7
ugandanCities = tuple(["Lira", "Oyam", "Mbarara", "Kasese"])
print(ugandanCities)

#8
phone1, phone2, phone3, phone4 = x
print(phone1), print(phone2), print(phone3), print(phone4)

#9
print(ugandanCities[1:4])

#10
firstNames = ("Ojok", "Opio", "Okello")
secondNames = ("Emmanuel", "Daniel", "Innocent")
fullNames = tuple(zip(firstNames, secondNames))
print(fullNames)

#11
colors = ("red", "green", "blue")
multi = colors * 3
print(multi)

#12
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count = thistuple.count(8)
print(count)


# SETS

#1
favouriteBeverages = set(["Soda", "Juice", "Beer"])
print(favouriteBeverages)

#2
favouriteBeverages.add("Yoghurt")
favouriteBeverages.add("water")
print(favouriteBeverages)

#3
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave in set.")
else:
    print("Microwave not in set.")

#4
mySet.remove("kettle")
print(mySet)

#5
for item in mySet:
    print(item)

#6
setItems = {1, 2, 3, 4}
listItems = [5, 6]
setItems.update(listItems)
print(setItems)

#7
ages = {10, 11, 27}
firstNames = {"Emmanuel", "Peter", "John"}
setAgesNames = ages.union(firstNames)
print(setAgesNames)


# STRINGS

#1
num = 56
str = "fifty six"
numStr = str(num) + str
print(numStr)

#2
txt = "      Hello,       Uganda!       "
formatedTxt = txt.replace(" ", "")
print(formatedTxt)

#3
formatedTxtUpper = formatedTxt.upper()
print(formatedTxtUpper)

#4
txtReplace = formatedTxtUpper.replace('U', 'V')
print(txtReplace)

#5
y = "I am proudly Ugandan"
myChars = y[1:4]
print(myChars)

#6
x = 'All "Data Scientists" are cool!'
print(x)


# DICTIONARIES

#1
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(Shoes["size"])

#2
Shoes["brand"] = "Adidas"
print(Shoes)

#3
Shoes["type"] = "sneakers"
print(Shoes)

#4
keys = list(Shoes.keys())
print(keys)

#5
values = list(Shoes.values())
print(values)

#6
if "size" in Shoes:
    print("The key 'size' exists in dictionary.")
else:
    print("The key 'size' does not exist in dictionary.")

#7
for key, value in Shoes.items():
    print(key, value)

#8
del Shoes["color"]
print(Shoes)

#9
Shoes.clear()
print(Shoes)

#10
valDict = {"1": "one", "2": "two"}
valDictCopy = valDict.copy()
print(valDictCopy)

#11
dictNested = {
    "one": {"1": "value one"},
    "two": {"2": "value two"}
}
for key, value in dictNested.items():
    print(key, value)