import json
import sys
import os

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Please mention a name.'

@app.route('/<candidate>')
def usern(candidate):
    with open(candidate) as json_data:
        resume_data = json.load(json_data)
        return(json.dumps(resume_data, indent=4))

if __name__ == "__main__":
#    app.run()
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)

