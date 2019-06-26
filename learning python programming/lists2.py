#nested lists

heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64]]

#zip one lists with other
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 65]

zipped_list = zip(names, heights)
print(zipped_list) #returns <zip object at 0x7f1631e86b48>

#to see the nested lists
print(list(zipped_list))

#making lists using range
list1 = []
list1 = range(5, 15, 3)
print(list(list1))

#different methods in lists
first_names = ['Ainsley', 'Ben', "Chani", "Depak"]
age = []
age.append(42)
all_ages = age + [32, 41, 29]
name_and_age = zip(first_names, all_ages)
ids = range(4)
