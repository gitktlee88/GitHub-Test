import sys
from datetime import datetime
import smtpd
from getpass import getpass

# print(sys.path)


# 1, turnary conditional
condition = True

x = 1 if condition else 0
print(x)

# 2, Large numbers
num1 = 10_000_000_000
num2 = 100_000_000

total = num1 + num2
print(f'{total:,}')

# 3, opening/closing file 'with context manager'
with open('tips.py', 'r') as f:
    file_contents = f.read()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)

# 4, enumerate function
names = ['Corey', 'Chris', 'Dave', 'Travis']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

# for index, name in enumerate(names, start=1):
#     print(index, name)
# for name, hero, universe in zip(names, heroes, universes):
#     print(f'{name} is actually {hero} from {universe}')
for value in zip(names, heroes, universes):
    print(value)

# 5, unpacking
# a, b, *c = (1, 2, 3, 4, 5)
a, b, *c, d = (1, 2, 3, 4, 5)
a, b, *_ = (1, 2, 3, 4, 5)

print(a)
print(b)
print(c)
print(d)

# 6, getting/setting attribute


class Person():
    pass


person = Person()

person_info = {'first': 'Corey', 'last': 'Schaufer'}

for key, val in person_info.items():
    setattr(person, key, val)

for key in person_info.keys():
    print(getattr(person, key))

# 7, inputting secrete information

# username = input('Username: ')
# password = getpass('Password: ')

print('Logging in...')

# 8, python -module
# python -m smtpd -c DebuggingServer -n localhost:1025
# how to find the options above
# help(smtpd)
# print(dir(datetime))

import requests

r = requests.get("https://google.com")
print(r.status_code)
print(r.ok)