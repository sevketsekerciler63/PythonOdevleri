fruits = ["apple", "banana", "orange"]
fruits.append("mango")
print(fruits)

my_list = [1, 2, 3, 4, 5]
new_list = my_list.copy()
print(new_list)

my_list = [1, 2, 2, 3, 4, 2, 5, 2]
count = my_list.count(2)
print(count)

fruits = ["apple", "banana", "orange", "mango"]
print(fruits)

my_list = [10, 20, 30, 40, 50]
del my_list[2]
print(my_list)

fruits = ["apple", "banana", "orange"]
more_fruits = ["mango", "grape"]
fruits.extend(more_fruits)
print(fruits)

my_list = [10, 20, 30, 40, 50]
print(my_list[0])
print(my_list[-1])

my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 6)
print(my_list)

my_list = [10, 20, 30, 40, 50]
my_list[1] = 25
print(my_list)

my_list = [10, 20, 30, 40, 50]
removed_element = my_list.pop(2)
print(removed_element)
print(my_list)

my_list = [10, 20, 30, 40, 50]
removed_element = my_list.pop()
print(removed_element)
print(my_list)

my_list = [10, 20, 30, 40, 50]
my_list.remove(30)
print(my_list)

my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)

my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])
print(my_list[:3])
print(my_list[2:])
print(my_list[::2])

my_list = [5, 2, 8, 1, 9]
my_list.sort()
print(my_list)

my_list = [5, 2, 8, 1, 9]
my_list.sort(reverse=True)
print(my_list)


fruits = ("apple", "banana", "apple", "orange")
print(fruits.count("apple"))

fruits = ("apple", "banana", "orange", "apple")
print(fruits.index("apple"))

numbers = (10, 20, 5, 30)
print(sum(numbers))

numbers = (10, 20, 5, 30)
print(min(numbers))
print(max(numbers))

fruits = ("apple", "banana", "orange")
print(len(fruits))














dict_name = {}
person = {"name": "John", "age": 30, "city": "New York"}

name = person["name"]
age = person["age"]

person["Country"] = "USA"
person["city"] = "Chicago"

del person["Country"]

person.update({"Profession": "Doctor"})

grades = {"math": 90, "science": 85}
grades.clear()

if "name" in person:
    print("İsim sözlükte mevcut.")

new_person = person.copy()
new_person = dict(person)

person_keys = list(person.keys())
person_values = list(person.values())
info = list(person.items())

empty_set = set()
fruits = {"apple", "banana", "orange"}
colors = {"orange", "red", "green"}

fruits.add("mango")
fruits.clear()
fruits = {"apple", "banana", "orange"}

new_fruits = fruits.copy()

fruits.discard("apple")

is_subset = fruits.issubset(colors)
is_superset = colors.issuperset(fruits)

removed_fruit = fruits.pop()

fruits = {"apple", "banana", "orange"}
fruits.remove("banana")

fruits = {"apple", "banana", "orange"}
colors = {"orange", "red", "green"}

combined = fruits.union(colors)
common = fruits.intersection(colors)
unique_to_fruits = fruits.difference(colors)
sym_diff = fruits.symmetric_difference(colors)

fruits.update(["kiwi", "grape"])

