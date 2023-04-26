from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
  return 'API Works!'
  
@app.route('/products')
def products():
  data = pd.read_csv('products.csv')
  return data.to_json()

# ---- Run this commands below to start server ----
# set FLASK_APP = app.py 
# flask run