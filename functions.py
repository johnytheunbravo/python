def greet(name):
    return f"Hey {name}!"

print(greet("Mattan"))
print(greet("Chris"))

def concatenate(word_one,word_two):
    return word_one + word_two

print(concatenate("Mattan","Griffel"))

# def age_in_dog_yr(age):
#     return age * 7
def age_in_dog_yr(age):
    result = age * 7
    return result

print(age_in_dog_yr(20))
# def is define and return is what you get back from that def fn
# can only do one return; or else return a list and or a dictionary 
# functions inside a function is possible 
# can define before (all)

# print(greet('mattan','this is one argument too many')) #wont run
# print(greet())
print(concatenate(word_two="Mattan",word_one="Griffel"))

name = "Mattan"
def print_diff_name():
    name = 'Chris'
    print(name)

print(name)
print_diff_name()
print(name)
# this is scoping i.e function only runs in their own world 