import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')

length = len(countries)
print(countries[1])
print(countries)

# Start your search algorithm here.

countries = ['Afghanistan, Bahamas, Cambodia, Denmar, Ecuador, Fiji , Gabon , Haiti, Iceland, Jamaica, Kenya, Laos, Mexico, Namibia', 'USA']

length = len(countries)
#length = 14

half = length/2
#half = 7 (between fiji & gabon)

country = input()

letter = index(country)
#Afghanistan index is A


first = countries[0]
last = countries[-1]
half = length/2

for first=0, first<=half, first++:
