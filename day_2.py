## Strings
course = "Python for beginners"
         #01234567
print(course.upper())       #change the case and return
print(course.find('for'))   #find for a str and return the index of the str
print(course.replace('for','4'))    # replace str with desired str
#print(course.__contains__('Python'))
check = 'Python' in course          # check if a str is in a str/variable.
print(check)


# Artithmatic

print(10+3.2 + 10//3.2 + 10/3.2 + 10-3.2)       # can do basic math on any numbers
print(10%3, "   ", 10**3)       # calculate remainder and power

x = 10
x = x+3
x += 3      # augmented assignment operator. can be used with all arithmatic operators
x **= 3
print(x)

