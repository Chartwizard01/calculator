welcome_message = ('Dear user, we are glad to have you on this platform where miracle is the order of the day, \n kindly supply us some details to help us know you better.  \n remain blessed')
print(welcome_message)

first_name = input('FIRST NAME: \n   ')
last_name = input('LAST NAME: \n   ')
part = 10
whole = 100
salary = input('how much do you earn as salary:  N')

if salary.isdigit():
    salary = float(salary)

tithe = (part/whole) * salary

message = f"Hello  {first_name} {last_name}, according to the salary detail provided above, you are to pay tithe of N{tithe} to the church account, \n WARNING: don't pay less unless you want God to stop blessing you"
print(message)

