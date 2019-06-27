#project to practice list comprehension and loops in python


hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for price in prices:
  total_price += price

average_price = total_price / len(prices)
print(average_price)

#cut the prices of each hairstyle by 5
new_prices = [price - 5 for price in prices]
print(new_prices)

#revenue of last week
total_revenue = 0
for i in range(len(hairstyles)):
	total_revenue += prices[i] * last_week[i]
  
print(total_revenue)

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

#haircuts under 30 according to new_prices
cuts_under_30 = [hairstyle for hairstyle in hairstyles if new_prices[hairstyles.index(hairstyle)] < 30]

print(cuts_under_30)

#random programs on list comprehension and loops

def divisible_by_ten(num):
  list = [i for i in num if i % 10 == 0]
  return len(list)
print(divisible_by_ten([20, 25, 30, 35, 40]))


def add_greetings(names):
  list = []
  for name in names:
    list.append("Hello, " + name)
  return list
print(add_greetings(["Owen", "Max", "Sophie"]))


def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

def odd_indices(lst):
  list = []
  i = 1
  while i < len(lst):
    list.append(lst[i])
    i += 2
  return list
print(odd_indices([4, 3, 7, 10, 11, -2]))


def exponents(bases, powers):
  list = []
  for base in bases:
    for power in powers:
      list.append(base**power)
  return list
print(exponents([2, 3, 4], [1, 2, 3]))
