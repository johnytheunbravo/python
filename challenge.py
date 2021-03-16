# uppercase and reverse = banana and should get back ANANAB print the result

def uppercase_and_reverse(word):
    result = word[::-1]
    return result
print(uppercase_and_reverse("do not go gentle into that good thing").upper())
print(uppercase_and_reverse("lol i forgot what mattan asked me to type.").upper())
print(uppercase_and_reverse("banana").upper())
# if you want to form a function
def uper_rev(x):
    return x.upper()[::-1]
print(uper_rev("banana"))