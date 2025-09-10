strings = [
    "abc123",
    "hello456world",
    "789",
    "test"
]

num_list = [nums for items in strings for nums in items if nums.isdigit()]
print(num_list)