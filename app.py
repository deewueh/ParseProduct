from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/main')
def mainPage():
    return render_template('main.html')


@app.route('/about')
def aboutPage():
    return render_template('about.html')


@app.route('/viewDataPage')
def viewDataPage(site1, site2):
    return render_template('viewData_Page.html')


@app.route('/enterDataPage')
def enterDataPage(site1, site2):
    return render_template('enterData_Page.html')


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/next')
def next_page():
    return render_template('next_page.html')


if __name__ == "__main__":
    app.run( debug=True )






