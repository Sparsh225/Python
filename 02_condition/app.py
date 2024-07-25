age=int(input("Enter a age :"))

# if age < 21:
#     print("Child")
# elif age >=13  and age <=19:
#     print("Teenager ")
# elif age >=20 and age <=59:
#     print("Adult")
# else:
#     print("Senior")

#movie ticket

day=str(input("Enter a day"))

if age >= 18:
    price=12
elif age <18:
    price=8
if day == "wednesday":
    price=price-2
print(price)