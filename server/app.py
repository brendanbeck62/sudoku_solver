import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv


load_dotenv(dotenv_path='../.env')

# configuration
PORT = os.environ.get('FLASK_PORT') or 5000

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
  return jsonify('pong!')

@app.route('/', methods=['GET'])
def home():
  return jsonify('hello world!')

if __name__ == '__main__':
  app.run(port=PORT)