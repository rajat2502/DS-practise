import requests
from bs4 import BeautifulSoup

webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
#print(webpage)
print(webpage_response.text) #gives html fully spaced and indented

#using beautiful soup library

soup = BeautifulSoup(webpage, 'html.parser')
print(soup) #beautifies the code!!!

#to access the content of the html code
print(soup.div.name) #to get the tagname -- will print div
print(soup.div.attrs) #to get the attributes of the tag
print(soup.p) #to get the first p tag
print(soup.p.string) #to get the string inside the first p tag

#navigating using .children and .parents
for child in soup.div.children:
  print(child)

for parent in soup.div.parents:
  print(parent)
  
#find_all() method
turtle_links = soup.find_all("a")
print(turtle_links)

#.select() to select elements using css selectors
turtle_links = soup.find_all("a")
links = []
#go through all of the a tags and get the links associated with them:
for a in turtle_links:
    links.append(prefix+a["href"])
    
#Define turtle_data:
turtle_data = {}

#follow each link:
for link in links:
  webpage = requests.get(link)
  turtle = BeautifulSoup(webpage.content, "html.parser")
  #Add your code here:
  turtle_name = turtle.select(".name")[0]
  turtle_data[turtle_name] = []
  
print(turtle_data)




