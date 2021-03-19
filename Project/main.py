
# import datetime module
import datetime
# import pymongo module
import pymongo
import dns
# connection string
client = pymongo.MongoClient(
    "mongodb+srv://admin:gmJR1NOhBmEEQm9t@cluster0.c8eub.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# test
try:
    db = client['ayuda_humanitaria']
    # define collection
    collection = db['sede']
    if db:
        print('✅ Coneccion establecida ')

except Exception as e:
    print('❌ Coneccion no establecida')
    print(e)
'''
# sample data
document = {"ciudad":"Capital One",
"direccion":"McLean",
"director":"VA"}
# insert document into collection
id = collection.insert_one(document).inserted_id
print("id")
asdasd
'''
