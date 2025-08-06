data = [
    [1,2,3],
    [4,5,6]
]

transpose_list = [[item[i] for item in data] for i in range(len(data[0]))]
print(transpose_list)