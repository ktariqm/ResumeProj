import json
import sys

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Please mention a name.'

@app.route('/resume')
def resume():
    try:   
        candidateName = request.args.get('name')
        resumeSection = request.args.get('section')
        with open(candidateName) as json_data:
            resume_data = json.load(json_data)
            if resumeSection:
                return(json.dumps(resume_data[resumeSection]))
            else:
                return(json.dumps(resume_data))
    except:
        return('Incorrect query format')

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)

