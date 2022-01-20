from distutils.log import debug
from flask import Flask, render_template
app = Flask(__name__)

# method for main page
@app.route('/')
def index():
    return render_template('index.html')

# method for dashboard page
@app.route('/dash')
def dash():
    return render_template('dash.html')


if __name__== '__main__':
    app.run(debug=True)
