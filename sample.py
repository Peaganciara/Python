print("Hello World")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
character_name = "Mike"
character_age = "70"
is_male = False
print("There once was a man named " + character_name + ",")
print(" " + character_name +" was " + character_age + " years old")
print("he liked his name " + character_name + ",")
print("But he did not like being " + character_age + ".\n")


# Text and stories in python are strings but for age you can store as a number so instead of typing out "70" it will
# be 70

# a boolean value represents a truth value that is true or false
#escape character \n allows you to skip line
# strings are plain text that we can store in python. need to use quotation marks

print("Peagan Mitchell")
# concatenation is the process of merging two or more strings

phrase="Peagan Mitchell"
print (phrase + " is an awesome analyst")

print (phrase.lower())
#the function lower makes the text lowercase
print (phrase.upper())

# isupper or islower will give back a true or false value depending if phrase is all upper or lower case
print(phrase.isupper())
print(phrase.islower())
#can use functions in combination
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
#brackets tell you what character is at length defined
print(phrase[5])
#0=first character in line
