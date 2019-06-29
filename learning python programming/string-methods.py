#split function
spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)

#join method
# 'delimiter'.join(list that u wish to join)

string = '\n'.join(spring_storm_lines)
print(string)

#example 2
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)
print(reapers_line_one)

#example 3
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)
print(winter_trees_full)

#.strip() method

featuring = "           rob thomas                 "
stripped_str1 = featuring.strip()
print(stripped_str1)

#example 2
featuring = "!!!rob thomas       !!!!!"
stripped_str1 = featuring.strip('!')
print(stripped_str1)

#miscelleous example
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
for item in love_maybe_lines:
	love_maybe_lines_stripped.append(item.strip())
  
print(love_maybe_lines_stripped)

love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)

#replace function
# .replace(str to be replaced, str to replace)

toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')
print(toomer_bio_fixed)

#find function
god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find('disown')
print(disown_placement)

#format() function
def poem_title_card(poet, title):
  return '''The poem "{}" is written by {}.'''.format(title, poet)

string = poem_title_card("Walt Whitman", "I Hear America Singing")
print(string)

#example 2 with keywords to improve code readibility
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date,author = author,title = title, original_work = original_work)
  return poem_desc

my_beard_description = poem_description("1974","Shel Silverstein", "My Beard", "Where the Sidewalk Ends")

print(my_beard_description)




















