urls = [
    "http://example.com",
    "https://secure-site.com",
    "ftp://files.example.org",
    "https://another-secure-site.com"
]

url_list = [items for items in urls if 'https' in items]
print(url_list)