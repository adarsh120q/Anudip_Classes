'''
Syntax:
    generator = (expression for item in iterable if condition)
Explanation
● generator :This is an assignment statement. The generator expression is
    assigned to a variable, typically called generator or gen, but any valid variable
    name can be used.
● (expression for item in iterable if condition) :`This is the core syntax of the
    generator expression, which is similar to list comprehensions but enclosed in
    parentheses () instead of square brackets [].
● Expression: This is the value that will be yielded by the generator. It’s typically
    an operation or function applied to each item in the iterable.
'''

gen = (x**2 for x in range(5))

for num in gen:
    print(num)