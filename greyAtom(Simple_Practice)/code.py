# --------------
# Code starts here

# creating lists
class_1 = [ 'Geoffrey Hinton', 'Andrew Ng', 'Sebastian Raschka', 'Yoshua Bengio' ]
class_2 = [ 'Hilary Mason', 'Carla Gentry', 'Corinna Cortes' ]

# concatinating lists
new_class = class_1 + class_2

# looking at the resultant list
print(new_class)

# appending 'Peter Warden' to new_class
new_class.append('Peter Warden')

# looking at the resultant list
print(new_class)

# deleting 'Carla Gentry' from list
new_class.remove('Carla Gentry')

# looking at the resultant list
print(new_class)

# Code ends here


# --------------
# Code starts here

# creating courses dictionary
courses = { 'Math':65,
            'English':70,
            'History':80,
            'French':70,
            'Science':60 }
# looking at the marks obtained in each subject
print(courses)

# calculating total
total = sum(courses.values())

# looking at the resultant list
print(total)

# calculating %
percentage = (total/500)*100

# printing the percentage
print(percentage)

# Code ends here


# --------------
# Code starts here

# Creating the dictionary
mathematics = { 'Geoffrey Hinton':78, 'Andrew Ng':95, 'Sebastian Raschka':65, 'Yoshua Benjio':50, 'Hilary Mason':70, 'Corinna Cortes':66, 'Peter Warden':75 }

# Calculating max 
topper = list(mathematics.keys())[list(mathematics.values()).index(max(mathematics.values()))]

# printing the name of student with maximum marks
print(topper)

# Code ends here  


# --------------
# Given string
topper = 'andrew ng'

# Code starts here

# Preparing full name to print in the certificate
last_name  = (topper.split()[-1])
first_name = (topper.split()[-2])
full_name = last_name + ' ' + first_name

# preparing certificate_name
certificate_name = full_name.upper()

#looking at the result :)
print(certificate_name)

# Code ends here


