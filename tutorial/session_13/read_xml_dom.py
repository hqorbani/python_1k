from xml.dom import minidom

file_data = minidom.parse('files/xml/food_menu.xml')

# food_tag = file_data.getElementsByTagName('food')
# print(food_tag[0].attributes['id'].value)
# child_data = food_tag[0].firstChild.data


name_tag = file_data.getElementsByTagName('name')

# one specific item attribute
child_data = name_tag[0].firstChild.data

print(type(child_data))
print("test:",child_data)