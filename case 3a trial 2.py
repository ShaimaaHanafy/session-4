import random
import string

# list which use from
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

random.letters1= ''.join(random.choice(letters))
random.letters2= ''.join(random.choice(letters))
random.letters3= ''.join(random.choice(letters))
random.letters4= ''.join(random.choice(letters))
random.symbols1= ''.join(random.choice(symbols))
random.symbols2= ''.join(random.choice(symbols))
random.numbers1= ''.join(random.choice(numbers))
random.numbers2= ''.join(random.choice(numbers))
random.numbers3= ''.join(random.choice(numbers))
characters=[random.letters1+random.letters2+random.letters3+random.letters4+random.symbols1+random.symbols2+random.numbers1+random.numbers2+random.numbers3]

#characters=string.ascii_letters+string.symbols+string.numbers
password=''.join(random.choice(characters))
print(password)
