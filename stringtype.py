# strings are text surrounded by quotes
#  bith (') or double (") or triple (""") quotes are used
# eg: "dinosaurs", '2112', "I'm lovin' it!"

kanye_quote = """My greatest pain in life
 is that I will never be able
 to see myself perform live."""
# can only shift text to another line if in triple quote
print(kanye_quote)
# can also use /n to move to new line
hamilton_quote = 'Well, the word got around, they said, "This kid is insane, man"'
print(hamilton_quote)

another_quote = """Well, the word got around, they said, "This kid's insane, man" """
yet_another = "Well, the word got around, they said, \"This kid is insane, man\""
name = "Tanishi Gupta" #varaiable assignment variable = left
orphan_fee = 200
teddy_bear_fee = 121.80

total = orphan_fee + teddy_bear_fee

# print(name,"the total will be",total)
print(f"{name} the total will be ${total:.2f}") # to only get this line 
# to round off to 2 even if more nos are present
