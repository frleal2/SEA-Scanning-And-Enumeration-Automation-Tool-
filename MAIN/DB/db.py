import pymongo
from pymongo import MongoClient

class databaseHandler():

#Initialize connection
    def __init__(self):
        self.cluster = pymongo.MongoClient("mongodb+srv://Admin:12345@cluster0.4cco1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    
    def build(self): 
        databases = self.cluster.list_database_names()

        db = "SEA_TOOl"

        if db not in databases:
            self.database = self.cluster["SEA_TOOl"]   
            tool = self.database["Tool"]
        
            Tool_Specs = {
                'name': "",
                'description': "",
                'path': "",
                'option': "", 
                'outputElement': "",
                'outputDataType': ""
            }
            
            tool.insert_one(Tool_Specs)

            print("*************************DATABASE CREATED**********************")

        else:
            self.database = self.cluster[db]
            print("************************DATABASE ALREADY CREATED*****************")

    def insertIntoTool(self, name, description, path, option, outputElement, outputDataType):
        tool = self.database["Tool"]
        
        Tool_Specs = {
            'name': name,
            'description': description,
            'path': path,
            'option': option, 
            'outputElement': outputElement,
            'outputDataType': outputDataType
        }
        tool.insert_one(Tool_Specs)
        

        