"""
A program that takes a letter and outputs a text file of
all of the countries that start with that letter
"""

# Todo: Read data/countries.txt and save all countries
countries =[]
with open('data/countries.txt','r') as file:
    for country in file.readlines():
        countries.append(country.strip())

print(countries)
print(len(countries))
# Get user to provide a letter
letter = input('Number of countries that start with letter: ')
letter = letter.capitalize()

# Todo: Print the number of countries that start with the letter
letter_countries =[]
for country in countries:
    if country.startswith(letter):
        letter_countries.append(country)

print(f" country is letter {len(letter_countries)}")
print(f" country is letter {letter_countries}")

# Todo: Create text file that lists the countries starting with the letter
with open(f'data/{letter}_countries.txt','w') as file:
    for country in letter_countries:
        file.write(country)
        file.write('\n')