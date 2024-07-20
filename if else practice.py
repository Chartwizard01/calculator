# list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# for number in list:
#     if number == "1":
#         print("1st")
#     elif number == "2":
#         print("2nd")
#     elif number == "3":
#         print("3rd")
#     else:
#         print(f"{number}th")

list = list(range(1,10))

for number in list:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")

# car_1 = {"engine": "v6" , "color":"black", "product": "Toyota", "model":"camry"}

# print(car_1["color"])
# print(car_1["engine"])
# print(car_1["model"])