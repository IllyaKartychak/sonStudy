import getpass


user_name = input("Enter your name")
print(user_name.upper())


some_row = input("Enter some row")
print(some_row.capitalize())

some_row2 = input("Enter some row ")
print(f"{some_row2.count("a")=}")

user_password = getpass.getpass("Enter password")
print(f"{user_password.isdigit()=}")

some_row3 = input("Enter some row")
print(some_row3.replace(" ", "_"))


some_row4 = input("Enter some row")
print(some_row4.startswith("Н"))


some_row5 = input("Enter some row")
print(some_row5.endswith("."))


some_row6 = input("Enter some row")
print(
    some_row6.strip(),
    some_row6.replace(
        "i1",
        "12",
    ),
)
