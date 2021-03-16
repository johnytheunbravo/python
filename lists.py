the_count = [1,2,3,4,5,6]
stocks = ["AAPL","GOOG","TSLA"]
random_things = ["Puppies",55,"Anthony Weiner", 1/2, ["Oh no","A list inside another list"]]

# this for-loop goes through a list
for number in the_count:
    print("this is count",number)

# same as the above
for stock in stocks:
    print("Stock ticker:",stock)

# for x in y:
# y here is the list which already exists while x is a variable which didnt previously exist
# we can go through mixed lists too
# i called it i since i dont knoe whats in it 
for i in random_things:
    print("Heres a random thing:", i)
# also build lists, first lets start with an empty one
people = []

people.append("Mattan")
people.append("Sarah")
people.append("Chris")

# now we can print them out too
print(people)

# and remove them too
people.remove("Sarah")
print(people)

for person in people:
    print("Person is:", person)
# challenge: Print out the squares of nos 1 to 10

print("_____________________________________________________________")

try_file = [1,2,3,4,5,6,7,8,9,10]
for numero in try_file:
    print("The square of the number", numero, "is", (numero * numero))
# for numero in list(range(1,11)):
#     print("The square of the number", numero, "is", (numero * numero))

# can also use
# for numero in [1,2,3,4,5,6,7,8,9,10]:
    # print("The square of the number", numero, "is", (numero * numero))

# to access elements on the list
animals = ['bear','tiger','penguin','zebra']
first_animal = animals[0] 
third_animal = animals[2]
print("there are this many things:", len(random_things))
print("things is a:", type(random_things))
another_list = random_things[4] #or [-1]
print(another_list)
print(type(another_list))
print(another_list[-1])


