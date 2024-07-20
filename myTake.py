welcome_message = """Dear user, we are glad to have you on this platform where miracle is the order of the day, \n kindly supply us some details to help us know you better.  \n remain blessed"""

print(welcome_message)

first_name = input("FIRST NAME: \n   ")
last_name = input("LAST NAME: \n   ")
# part = 10
# whole = 100
salary = input("how much do you earn as salary:  N")

# if salary.isdigit():
salary = float(salary)

tithe = salary * 0.1

message = f"Hello,  {first_name.title()} {last_name.title()}, according to the salary detail provided above, you are to pay tithe of N{tithe: ,.2f} to the church account. \n\n WARNING: Don't pay less unless you want God to stop blessing you"


print(message)
