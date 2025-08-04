my_list=[1,2,3,4,'Python',5.0,6.0]
print(my_list)
print(type(my_list))
'''
ele : 1 2 3 4 Python 5.0 6.0
idx : 0 1 2 3  4      5   6
o/p : 2, 4, 5.0
'''
print(my_list[1:7:2])
print(my_list[::])
print(my_list[::-1])# reverse order
my_list[2]=99# modify element at index 2
print(my_list)
print(len(my_list))
#functions for list
my_list.append(100);
my_list.append(110);
print(my_list)
my_list.insert(3,999);
print(my_list)
my_list1=[1,4,5,7,8,'A',7,8,6,'UI']
my_list.extend(my_list1)# at the end
print(my_list)
#removal
#remove() vs pop()
print(my_list.remove(1))# the specification of element not index
print(my_list)
print(my_list.pop(2))# the specification of index not element
print(my_list)
print(my_list.pop())
'''
Remove                                                        pop
1)specify element                                            1) specify index
2) it removes the element but will not return                2) it removes and returns the element
[2, 99, 4, 'Python', 5.0, 6.0, 100, 110, 1, 4, 5, 7, 8, 'A', 7, 8, 6]

'''
print(my_list.index(5))# returns the index of element 5
print(my_list.count(7))# returns the count of repetition of element 7
my_list.reverse()
print(my_list)
my_list3=[1,49,3,23,6,76,5]

sorted_list=sorted(my_list3)
print(sorted_list)
print(my_list3)
my_list3.sort()
print(my_list3)
#traversal functions
# using for loop
# 1 3 5 6 23 49 76
# for each
# enhanced for loop
for item in my_list3:
  print(item,end=" ")

print()
#use range and len
for i in range(len(my_list3)):
  print(my_list3[i],end=" ")
print()
# explore enumerate function
for index,element in enumerate(my_list3):
  print(f'Index : {index} Element : {element}')

# while loop
index=0
while index<len(my_list3):
  print(my_list3[index])
  index+=1

print(f'The last value of index is {index}')
