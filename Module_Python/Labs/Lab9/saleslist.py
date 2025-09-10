employees = [
    {"name": "John Doe", "department": "Sales"},
    {"name": "Jane Smith", "department": "Marketing"},
    {"name": "Emily Johnson", "department": "Sales"},
    {"name": "Michael Brown", "department": "HR"}
]

sales_list = [(items.get('name')).upper() for items in employees if 'Sales' in items.values()]
print(sales_list)