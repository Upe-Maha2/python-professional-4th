# VS code Extentions

# -Python (highlight code )
# -Black (suto format)
# -isort()

# print("Hello WOrld!")
# name_is = "Upendra"
# age_is = 21

# print(f"My name is {name_is}, and age is {age_is}")

# a = int(input("Enter the first number : "))
# b = int(input("Enter the second number : "))

# print(f"Result = {a + b}")

# age = int(input("Enter the age: "))

# if age < 18:
#     print("Minor")
# else:
#     print("Adult")


# for i in range(5):
# print(f"Hi {i}")


# def greet(name):
#     return f"Hello {name}"


# print(greet("Earth"))
# print(greet("Roshna"))
# print(greet("Ashish"))

# === HW ===
# two variables with values, if the values are greater then 10 do addition, else smaller than 10 do subtract,
# print message five time.

first_num = int(input('Enter the first number: '))
second_num = int(input('Enter the second number: '))
for i in range(5):
    if first_num > 10 and second_num > 10:
        add = first_num + second_num
        print(f"Addition{i} = {add} ")
    else:
        sub = abs(first_num - second_num)
        print(f"Subtractoin{i} = {sub}")


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Upendra", 21)
# print(s1.name)
# print(s1.age)

# GITHUB


# manual virtual environment creation
# python -m venv venv
# activate virtual environment
# source venv/bin/activate
