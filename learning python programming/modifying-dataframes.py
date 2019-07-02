import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add columns here
df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']

print(df)

#to add a column with same values to all rows
df['Is taxed?'] = 'Yes'
print(df)

# adding columns with functions
df['Revenue'] = df['Price'] - df['Cost to Manufacture']
print(df)

#modifying columns in a dataframe
df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
columns=['Name', 'Email'])

# Add columns here
df['Lowercase Name'] = df.Name.apply(lower)
print(df)

#lambda function
mylambda = lambda str : str[0] + str[-1]
print(mylambda('This is a string'))

#if else with lambda function
#basic syntax
#lambda x: [OUTCOME IF TRUE] \
 #   if [CONDITIONAL] \
 #   else [OUTCOME IF FALSE]
 #basic example
#myfunction = lambda x: 40 + (x - 40) * 1.50 \
#   if x > 40 else x

mylambda = lambda age: "Welcome to BattleCity!"\
	if age > 13 else "You must be over 13"
print(mylambda(12))

#performing operations on df column using a lambda
df = pd.read_csv('employees.csv')
get_last_name = lambda str: str.split(' ')[-1]
# Add columns here
df['last_name'] = df.name.apply(get_last_name)
print(df)

#applying lambda to a row
df = pd.read_csv('employees.csv')

total_earned = lambda row: (row.hourly_wage * 40) + ((row.hourly_wage * 1.5) * (row.hours_worked - 40)) \
	if row.hours_worked > 40 \
  else row.hourly_wage * row.hours_worked
  
df['total_earned'] = df.apply(total_earned, axis = 1)

print(df)

#renaming columns
#example
#df = pd.DataFrame({
#    'name': ['John', 'Jane', 'Sue', 'Fred'],
#    'age': [23, 29, 21, 18]
#})
#df.columns = ['First Name', 'Age']

df = pd.read_csv('imdb.csv')
orders = pd.read_csv('shoefly.csv')

print(orders.head(5))

orders['shoe_source'] = orders.shoe_material.apply(lambda x: \
                        	'animal' if x == 'leather'else 'vegan')

orders['salutation'] = orders.apply(lambda row: \
                                    'Dear Mr. ' + row['last_name']
                                    if row['gender'] == 'male'
                                    else 'Dear Ms. ' + row['last_name'],
                                    axis=1)
# Rename columns here
df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']
print(df)

#renaming individual columns
df = pd.read_csv('imdb.csv')

# Rename columns here
df.rename(columns = {
  'name': 'movie_title'
}, inplace = True)
print(df)

#practice


