from functools import reduce

lambda a: a * 2
multiply = lambda a, b: a * b
print(multiply(2, 9))

numbers = [1, 2, 3, 4]

# def double(a):
#     return a * 2
double = lambda a: a * 2


result = map(double, numbers)
print(list(result))


# def isEven(n):
#     return n % 2 == 0

# isEven = lambda n: n % 2 == 0


result2 = filter(lambda a: a % 2 == 0, numbers)
print(list(result2))


Expenses = [
    ('dinner', 80),
    ('car_repair', 120)
]
sum = reduce(lambda a, b: a[1] + b[1], Expenses)
print(sum)
