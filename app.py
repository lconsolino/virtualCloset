from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
from random import randint
import importCSV
from pprint import pprint
import CSVManager
import argparse


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def get_mailbox_callback():
    """
    Summary: A callback which for when GET is called on [host]:[port]/mailbox

    Returns:
        string: A JSON-formatted string containing the response message
    """
    if request.method == 'POST':
        user_text = request.form['user_input']
        response = clothing.findResult(user_text)
        pprint(response)
        # for i in enumerate(response):
        #     return render_template('result.html', data=response)
        if(response != None):
            return render_template('searchResult.html', data=response)
    return render_template('test.html',data= None)

@app.route('/result/<id>')
def result(id):
    item = next((entry for entry in clothing.dictionaryArr if entry.get('id') == id), None)
    return render_template('result.html',data=item)

@app.route('/search/<id>')
def search(id):
    response = clothing.getKeywordItems(id)
    pprint (response)
    if(response != None):
            return render_template('searchResult.html', data=response)
    return render_template('test.html',data= None)
# @app.route("/item" )
# def item():
#         category = request.args.get('key')
#         value = request.args.get('value')
#         pprint('path is item')
#         pprint(category)
#         pprint(value)
#         response = clothing.searchObjects(category,value)
#         pprint(response)
#         # response = jsonify(clothing.searchObjects(category,value))
#         # pprint(response)

#         # The object returned will be sent back as an HTTP message to the requester
#         return render_template('test.html',data=response)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='app',
            description='Script to start up wardrobe')

    args = parser.parse_args()

    clothing = CSVManager.clothingManager()
    app.run(debug=False, host='0.0.0.0', port=5000)   

