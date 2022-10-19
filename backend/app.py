from flask import Flask

# Sanitize user input to prevent SQL injection
from markupsafe import escape 

# Great React JS Helper Files on Digital Ocean
# https://www.digitalocean.com/community/tutorial_series/how-to-code-in-react-js

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello chess organiser, welcome to the future of organization</h1>'

@app.route('/tournaments/<int:tourn_id>')
def tournaments(tourn_id):
    return '<h1>{}</h1>'.format(escape(tourn_id))
