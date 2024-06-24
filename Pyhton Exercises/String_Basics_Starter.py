
first = "Nico"
last = "Hulkenberg"

# - Create a variable called "full_name" that combines first and last with a space between them.  
# - Print it out
full_name = first + " " + last
print(full_name)

# - Create an "initials" variable that holds the first character of first followed by the first character of last. 
# - Print it out
initials = first[:1] + last[:1]
print(initials)


# - Create an "initials_2" variable that holds the first character of first followed by the first character of last, with periods after each letter!
# - Print it out
initials_2 = first[:1] + last[:1]
print(first[:1] + "." + last[:1] + ".")

# Create a "nickname" variable that holds the first 4 characters of "last" (use a slice)
# Print it out 
nickname = last[:4]
print(nickname)

