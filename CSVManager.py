from datetime import datetime
from threading import Lock
import importCSV
import csv
from pprint import pprint

MAIL_REQ_FIELDS = ['subject', 'body', 'sender']
MAIL_DB_FILE = 'mail.pickle'
class clothingManager(object):
    def __init__(self):
        """
        Summary: Class for managing the dictionary of mail data and the pickle
                file used for persistent storage
        """

        print('starting manager')

        headers = ['id','gender','masterCategory','subCategory','articleType','baseColour','season','year','usage','productDisplayName']

        clothingFile = "styles.csv"

        columns =[]
        rows =[]
        dictionaryArr= []
        with open(clothingFile, 'r') as csvfile:
            readClothing= csv.reader(csvfile)
            columns=next(readClothing)
            for item in readClothing:
                rows.append(item)
        for row in rows[1:]:
            # parsing each column of a row
            lineDictionary={}
            for i, col in enumerate(row):
                if(i<len(headers)):
                    lineDictionary[headers[i]]=col
            dictionaryArr.append(lineDictionary)
        self.dictionaryArr=dictionaryArr
        self.headers=headers
        
    def searchObjects(self,key,value):
        
        pprint(value)
        pprint(key)
        if(key=='' and value ==''):
            return "no key value"
        for item in self.headers:
            pprint(item)
            if item == key:
                for object in self.dictionaryArr[1:]:
                    pprint(object[key])
                    if value in object[key]:
                        pprint(object[key] )
                        return object
        return "none found"

        # params ={
        #     key: value
        # }
        # response = requests.get("http://{}/item".format(self.serv_addr), params=params)
    def findResult(self,input):
        results = []
        for category in self.headers:
            for keyword in self.dictionaryArr[1:]:
                if input.lower() in keyword[category].lower():
                    pprint(keyword[category])
                    results.append(keyword)
                    # return keyword
            # if item == input:
            #     for object in self.dictionaryArr[1:]:
            #         pprint(object[input])
            #         if object[input] == input:
            #             pprint(object[input] )
            #             return object
        return results