#first exercise 3-4
# birthday_guests = ['Jonah', 'Cecilia', 'Michael', 'Hannah' ]

# invite_1= f'Hello Mr/Mrs {birthday_guests[0]}, i am delighted to invite you to my birthday party'

# invite_2= f'Hello Mr/Mrs {birthday_guests[1]}, i am delighted to invite you to my birthday party'

# invite_3= f'Hello Mr/Mrs {birthday_guests[2]}, i am delighted to invite you to my birthday party'

# invite_4= f'Hello Mr/Mrs {birthday_guests[3]}, i am delighted to invite you to my birthday party'

# #end of first exercise. you can print invite for any guest using print command and selecting the corresponding number

# for guest in birthday_guests: 
#     print(guest)

#USING FOR LOOP 

#birthday_guests = ['Jonah', 'Cecilia', 'Michael', 'Hannah' ]

# for guest in birthday_guests:
#     message = f"Dear {guest.title()}, I seek your honorable presence in my birthday party!!!"
#     comment = "come and lets spread love \n"
#     print(message)
#     print(comment)

# print("thank you everyone as you honor my invite")


#NUMERICAL ASPECT OF LIST

# for value in range(0,9):
#     print(value)

# number = list(range(1,7))

# lucky_number = number[2]
# print(lucky_number)
# names = ["sam", " jonah", " daniel"]
# other_names = ["mr mike", "mr sam"]
# new_list = [names, other_names]
# print(new_list[0][1])

#even_numbers = list((range(2,15,2)))
#print(even_numbers)

# odd_numbers = list(range(1,20,2))
# print(odd_numbers)

# Number = int(input("write a number:\n "))  #code to check if the user inputed number is an odd or even number 
# if Number % 3 == 0:
#     print("This an odd number! ")
# else:
#     print("This is an even number!")


# PLACES TO VIST

# location = ['Paris', 'Santorini', 'Hungary', 'Maldive', 'Canada','Athen','Dubai','USA','UK']

# for country in location:
#     print(country)

students = ["Ogbadu", "Ojodu", "Ojone", "Ojochide"]

students.append('Ojonide')
students.insert(2,'Ojoago')
students.append('Godwin')
qualified_students = students[:]

qualified_students.append("Moses")

print(f"the qualified students are: \n {students} \n")

print(f"\n while the students who sat for the exams are: \n { qualified_students}")