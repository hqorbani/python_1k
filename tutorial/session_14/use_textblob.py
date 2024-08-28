from textblob import TextBlob
from rw_files import *

# my_input = ("Sukanya, Rajib and Naba are my good friends. " +
#     "Sukanya is getting married next year. " +
#     "Marriage is a big step in one’s life." +
#     "It is both exciting and frightening. " +
#     "But friendship is a sacred bond between people." +
#     "It is a special kind of love between us. " +
#     "Many of you must have tried searching for a friend "+
#     "but never found the right one.")

my_input = "سلام، من یک برنامه نویس هستم. شما چطور؟"
# create a textblob object
blob_object = TextBlob(my_input)
 
# Part-of-speech tags can be accessed 
# through the tags property of blob object.'
 
# print word with pos tag.
print(blob_object.tags)

print(type(blob_object.tags))

# db_data = read_json_file('db.json')
# db_data.append(blob_object.tags)
# write_json_file('db.json' , db_data)



