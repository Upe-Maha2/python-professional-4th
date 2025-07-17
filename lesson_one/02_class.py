# from collections import defaultdict

# s = {1, 2, 3, 2, 4}
# # print(s)

# d = set()
# d.add(5)
# # print(d)

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# # print(s1.union(s2))
# # print(s1.intersection(s2))

# fs = frozenset([1, 2, 3, 3, 2])
# print(fs)

# s = {frozenset([1, 2]), frozenset([3, 4])}
# print(s)


# d = defaultdict(int)
# d['a'] += 1
# print(d)

# d2 = defaultdict(list)
# d2['a'].append(10)
# print(d2)


# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print(f"Result: {result}")
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Invalid input! Please enter a valid integer.")


import turtle
t = turtle.Turtle()
for i in range(100):
    t.forward(100)  # steps
    t.right(189)  # degrees
turtle.done()


#   DJango Project Setup# To create a Django project and app, run the following commands in your terminal:
# Make sure you have Django installed in your Python environment.
# django-admin startproject ecom
# django-admin startapp store
