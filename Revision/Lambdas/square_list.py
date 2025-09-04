li = [1,2,3,4,5]
# def sq(li):
#     new_li = []
#     for i in li:
#         new_li.append(i**2)

#     return new_li

# print(sq(li))

square = list(map(lambda x: x**2, li))
print(square)