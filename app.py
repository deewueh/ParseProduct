from flask import Flask, render_template
from main import get_soup_5ka
from main import get_soup_SberAshan
from main import test_excel

app = Flask(__name__)
my_instance = test_excel()
ashan_instance = get_soup_SberAshan()
vka_instance = get_soup_5ka()

@app.route('/')
@app.route('/main')
def mainPage():
    return render_template('main.html')


@app.route('/about')
def aboutPage():
    return render_template('about.html')


@app.route('/viewData')
def viewDataPage():
    return render_template('viewData_Page.html')


@app.route('/enterData')
def enterDataPage():
    return render_template('enterData_Page.html')

@app.route('/call_method')
def call_method():
    result = my_instance.test_excel()
    return result


@app.route('/call_ashan')
def call_method():
    result = ashan_instance.get_soup_SberAshan()
    return result


@app.route('/call_method_5ka')
def call_method():
    result = my_instance.get_soup_5ka()
    return result

if __name__ == "__main__":
    app.run( debug=True )

