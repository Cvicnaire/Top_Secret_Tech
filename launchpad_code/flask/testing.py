from flask import Flask
from markupsafe import escape
from flask import render_template
from flask import request
from flask import make_response
from flask import jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')



## Testing the form submit route
@app.route("/form_1")
def form_1():
    tasks = ['fastqc', 'bismark']
    parameters = ['param1', 'param2']
    workflows = [ 'wgbs', 'RNA-Seq']
    return render_template("form.html", tasks = tasks, parameters = parameters, workflows = workflows)

@app.route("/submit", methods = ['POST'])
def submit():
        
        data = {
            "key1": request.form.get('value1'),
            "key2": request.form.get('value2')
        }
        # url of the backend flask application
        url = 'http://127.0.0.1:5002/process'

        response = requests.post(url, json=data)
        
        return jsonify(response.json())





if __name__ == '__main__':
    app.run(debug=True)
