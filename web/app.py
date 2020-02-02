from flask import Flask
from web import app
from flask import request
app = Flask(__name__)
import requests
import json


#if database is not present create it 

db_url = "http://127.0.0.1:5984/highspot"
db_check = requests.get(db_url)

if str(db_check.status_code) != "200":
	print ("database not present creating it")
	try:
		create_db = requests.put(db_url)
	except:
		print ("Unable to create database")

count_url = "http://127.0.0.1:5984/highspot/doc_count"
count_check = requests.get(count_url)

if str(count_check.status_code) != "200":
	print ("Count document not present creating it")
	try:
		default_count = '{"count":0}'
		create_count = requests.put(count_url,default_count)
	except:
		print ("Unable to create count")

@app.route('/healthcheck')
def pingResponse():
	return "pong"

@app.route('/')
def index():
	app_url = "http://127.0.0.1:8000/"
	url1 = "http://127.0.0.1:5984/highspot/doc_count"
	try:
		db1 = requests.get(url1)
		couch = db1.json()
		
		return (str(app_url)+str(couch["count"]))
	except:
		print ("unable to query")
		return {"msg":"Unable to reach database","status": 400}

@app.route('/<doc_id>', methods=['GET', 'POST'])
def webhook(doc_id):
	if request.method == 'POST':
		base_url = "http://127.0.0.1:5984/highspot/"
		doc_url = base_url+str(doc_id)
		url1 = "http://127.0.0.1:5984/highspot/doc_count"
		status = None
		status = requests.get(doc_url)
		input_data = request.get_json(force=True)
		for key in input_data:
			if str(key)[0] == "_":
				return {"msg":" _ cannot be a prefix to any key","status":404}
		if (str(status.status_code)=="404"):
	    #document not present create it and update document code
	    		doc_count_update =  requests.get(url1)
	    		doc_count_data = doc_count_update.json()
	    		doc_count_data["count"]+=1
	    		update = requests.put(url1,json = doc_count_data)
	    		r = requests.put(doc_url,json=input_data)
	    		return str(r.status_code)
		else: 
			doc_data = status.json()
			input_data["_rev"]=doc_data["_rev"]
			input_data["_id"]=doc_data["_id"]
			r = requests.put(doc_url,json=input_data)
			return str(r.status_code)
	else:
		base_url = "http://127.0.0.1:5984/highspot/"
		doc_url = base_url+str(doc_id)
		db2 = requests.get(doc_url)
		returnData = db2.json()
		returnData.pop("_id",None)
		returnData.pop("_rev",None)
		return returnData
