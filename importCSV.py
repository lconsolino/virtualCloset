import csv
import json
from pprint import pprint
import requests
class clothing(object):
    def __init__(self,username, serv_addr):
        """
        Summary: Class that manages the HTTP interactions with a mailboxServer

        Args:
            username (string): Username that will identify the client for current session
            serv_addr (string): Target mailbox server to connect to in format ip_addr:port
            serv_password (string): Target mailbox server's password
        """
        self.username= username
        self.serv_addr= serv_addr
        
    def search_mail(self, field, text):
        # to edit
        """
        Summary: Sends a GET request to server for mail matching search parameters

        Args:
            field (string): One of the fields of the email (body, subject, sender, etc)
            text (string): Description
        """
        pprint(field)
        pprint(text)
        if field != None and text!= None:
            params = {
                'key': field,
                'value': text,
            }
            response = requests.get("http://{}/item".format(self.serv_addr), params=params)

        if response.status_code == 200:
            pprint(response)

        else:
            print('\n' + response.text)

# manager should have all clothing objects
# tools should be able to handle client commands and transfer to http requests to server
# server handles routes
# client handles laptop input
