name = []
name.append('samson')
name.append('david')
name.append('jerry')
name.append('hassan')
message = f"hello {name[0]} you are a special guest\nhello {name[1]} you are a special guest\nhello {name[2]} you are a special guest\nhello {name[3]} you are a special guest"
print (message)
new = f"sorry guys i just realized {name[1]} and {name[2]} won't be available for the event"
del name [1]
del name [2]
print (new)
name.insert (1,"john")
name.insert (3,"fred")
name.append ("job")
messages = f" these are the permanent homosapiens attending the event\n {name[0]}\n{name[1]}\n{name[2]}\n{name[3]}\n{name[4]}"
print (messages)
current_guest = f"hello {name[0]} you are a special guest\nhello {name[1]} you are a special guest\nhello {name[2]} you are a special guest\nhello {name[3]} you are a special guest \nhello {name[4]} you are a special guest"
print (current_guest)

print ("emergency,i can only invite two people,who is ready  to go with me")
stress = name.pop()
jober = f"sorry i could not invite you for this event {stress}"
print (jober)
tired = name.pop(-1)
fatigue =  f"sorry i could not invite you for this event {tired}"
print (fatigue)
wreck = name.pop(-2)
week = f"sorry i could not invite you for this event {wreck}"
print (week)
new_time =f"only {name} are invited now"
print (new_time)
del name[0]

print (name)

