import pymongo
from pymongo import MongoClient

class databaseHandler():

    def __init__(self):
        self.cluster = pymongo.MongoClient("mongodb+srv://Admin:12345@cluster0.4cco1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    
    def build(self): 
        db = self.cluster["SEA_TOOl"]   
        collection1 = db["Tool_Specification"]

        collection2 = db["Tool"]
        
        Tool_Specs = {
                'name': "",
                'description': "",
                'path': "",
                'option': "", 
                'outputElement': "",
                'outputDataType': ""
        }
        
        collection2.insert_one(Tool_Specs)

        print("*************************DATABASE CREATED**********************")

        