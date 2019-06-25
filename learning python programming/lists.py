# learning lists

friends = ["chandan", "nihal", "pragati", "mr single", "gaurav"]

'''
#multiline comment

friends[0] = "chandu"
print(friends)
print(friends[1])
print(friends[-1]) # gives last element
print(friends[2:]) #gets all the elements from it
print(friends[2:4]) #from 2 before 4'''

#lists methods

list_two = ["palak", "addy", "muskan", "nikhil"]

#to append one list to another

friends.extend(list_two)

#to append one more element to list to the end of the list

friends.append("nitish")

#to insert an element at a specified position

friends.insert(5, "diya")

#to remove elements from the lists
friends.remove("diya")

# to remove element from the end
friends.pop()

#to clear the lists
#friends.clear()

#to check the index of a particular element is in the lists
#print(friends.index("nihal"))

#to count the number of times an element is repeated in the list
#print(friends.count("chandan"))

#to sort the list in alphabetical order
friends.sort()
print(friends)

#number list 
lists = [4,5,3,2,5,25,25,25]
lists.sort()
print(lists)

#reverse a list
lists.reverse()
print(lists)

friends.reverse()
print(friends)

#copy a lists to another
my_friends = friends.copy()
print(friends)








