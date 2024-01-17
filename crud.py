from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):  
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:35825' % (user, password))
        self.database = self.client['AAC']  

    def create(self, data):
        """ Create method to add new data to collection """
        if data is not None:
            self.database.animals.insert_one(data)  
            print(" animal created successfully")  
        else:
            raise Exception("Nothing to save, because data parameter is empty")  

    def read(self, data):
        """ Read method to find documents from collection """
        if data is not None:
            data = self.database.animals.find(data, {"_id": False})  
            return data
        else:
            raise Exception("nothing to read, hint is empty") 

    def update(self, _keys, _data):
        """ Update method to modify documents in collection """
        if _data is not None and _keys is not None:
            self.database.animals.update_many(_keys, {'$set': _data})  
            data = self.read(_data)
            return data
        else:
            raise Exception("please Enter both key and data to modify the collection")  

    def delete(self, _data):
        """ Delete method to remove documents from collection """
        if _data is not None:
            data = self.read(_data)  
            if data is None:
                print("Animal not found")  
                return
            self.database.animals.delete_many(_data)  
            data = self.read(_data)  
            return data
        else:
            raise Exception("nothing to read, hint is empty")  



