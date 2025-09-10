emails = [
    "alice@example.com",
    "bob@sample.org",
    "charlie@mydomain.net"
]

domain_list = [items[items.index('@')+1:] for items in emails]
print(domain_list)