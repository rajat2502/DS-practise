from datetime import datetime

birthday = datetime(2000, 2, 25, 6, 15, 10)
print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.hour)
print(birthday.weekday()) #monday as 0 and so on

print(datetime.now())


#we can also subtract datetime
print(datetime(2018, 1, 1) - datetime(2017, 1,1))

#using strptime funciton -- allow us to fromat a string into datetime
date = 'jan 15, 2018'
parsedate = datetime.strptime(date, '%b %d, %Y') #takes two arguements one our string and other telling our format of the string
print(parsedate)

#using strftime function -- used to format a datetime into a string
date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string)
