from flask import Flask, render_template

app = Flask(__name__)
@app.route('/main')
def mainPage():
    return "Всем привет!"


@app.route('/about')
def aboutPage():
    return "О проекте"


@app.route('/about')
def viewDataPage(site1, site2):
    return "ViewDataPage: " + site1 + site2


if __name__ == "__main__":
    app.run( debug=True )