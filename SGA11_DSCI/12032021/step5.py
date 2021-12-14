from step4 import requestResults

from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

# start flask
app = Flask(__name__)
# app = Flask(__name__, template_folder='pages')

# render default webpage
@app.route('/')
def home():
    return render_template('home.html')

# when the post method detect, then redirect to success function
@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return redirect(url_for('success', name=user))

# get the data for the requested query
@app.route('/success/<name>')
def success(name):
    name = pd.read_csv('data/twitter_sentiments.csv')
    return "<xmp>" + str(requestResults(name)) + " </xmp> "


if __name__ == '__main__':
    app.run(debug=True)