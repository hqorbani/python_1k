import xml.etree.ElementTree as ET

tree = ET.parse('files/xml/books.xml')
root = tree.getroot()

print(type(tree))
print()
print(root)
for book in root.findall("book"):
    title = book.find('title')
    author = book.find('author')
    price = book.find('price')
    print(title , author , price)
