#Strings

#This would be the str
#xero is my name
#"xero is my name"
#null is my last name
#"null is my last name"
#"XERO NULL"
#xeronull

#using the proper syntax that python can interpret printing xero and null on seperate lines
first_name = "xero"
print(first_name)
last_name = "null"
print(last_name)

#concatenating first and last name
full_name = first_name + " " + last_name

#captilize and concatenating first name and last name and adding a space between
print(first_name.upper() + " " + last_name.upper())

#print full_name in lowercase
message = "xeronull"
message = message.lower()
print(message)

# then count how many x's are in full_name
x_count = message.count("x")
print("Our message has " + str(x_count) + " x's in it.")

# first_name = "xero"
# last_name = "null"
# print(full_name + last_name)

