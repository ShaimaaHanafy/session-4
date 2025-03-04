import random
import string

# list which use from
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

random.list1= ''.join(random.choice(letters+symbols+numbers))
random.list2= ''.join(random.choice(letters+symbols+numbers))
random.list3= ''.join(random.choice(letters+symbols+numbers))
random.list4= ''.join(random.choice(letters+symbols+numbers))
random.list5= ''.join(random.choice(letters+symbols+numbers))
random.list6= ''.join(random.choice(letters+symbols+numbers))
random.list7= ''.join(random.choice(letters+symbols+numbers))
random.list8= ''.join(random.choice(letters+symbols+numbers))
random.list9= ''.join(random.choice(letters+symbols+numbers))
characters=[random.list1+random.list2+random.list3+random.list4+random.list5+random.list6+random.list7+random.list8+random.list9]

#generate password
password=''.join(random.choice(characters))
print(password)
