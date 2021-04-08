import pymongo
from pymongo import MongoClient
import pandas as pd

class databaseHandler():

#Initialize connection
    def __init__(self):
        self.cluster = pymongo.MongoClient("mongodb+srv://Admin:12345@cluster0.4cco1.mongodb.net/test?authSource=admin&replicaSet=atlas-2cze3m-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
    
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
                'outputDataSpec': "",
                'optionAndArgument': ""
            }
            
            tool.insert_one(Tool_Specs)

            print("*************************DATABASE CREATED**********************")

        else:
            self.database = self.cluster[db]
            print("************************DATABASE ALREADY CREATED*****************")

    def insertIntoTool(self, name, description, path, outputDataSpecification, optionAndArg):
        tool = self.database["Tool"]
        
        Tool_Specs = {
            'name': name,
            'description': description,
            'path': path,
            'outputDataSpec': outputDataSpecification,
            'ouptionAndArgument': optionAndArg
        }
        tool.insert_one(Tool_Specs)
        print ("********** INSERTED INTO TABLE*****************")
    
    def deleteFromTool(self,name):
        tool = self.database["Tool"]
        some_query = {"name" : name}
        
        result = tool.delete_one( some_query )
        print ("result:", type(result), "-- deleted count:", result.deleted_count)    

    def updateAtTool(self, name, name2, description, path, outputDataSpecification, optionAndARg):
        print(name, name2)
        tool = self.database["Tool"]
        query = { "name": name }
        newvalues = { "$set": { "name": name2,
                                "description": description,
                                "path": path,
                                "outputDataSpec": outputDataSpecification,
                                "ouptionAndArgument": optionAndARg} 
                    }
        result = tool.update_one(query, newvalues)
        print ("acknowledged:", result.acknowledged)


    def importData(self):
        tool = self.database["Tool"]
        data = pd.DataFrame(list(tool.find()))
        return data
        