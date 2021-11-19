from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient() #connects to the local host, default port mongo server (which is what we have!)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/count')
def get_count():
  return str(client.db['CS301'].count_documents({}))