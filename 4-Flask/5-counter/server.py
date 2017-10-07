
from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'counter123456789'

# METHOD 1: Check if KEY is in session (DICTIONARY)
# @app.route('/', methods=['GET'])
# def index():
#     for keys in session:
#         if keys == 'counter':
#             session['counter'] += 1
#         else:
#             session['counter'] = 1
#     return render_template("index.html")

# METHOD 2: Use TRY & EXCEPT, which employs a countermeasure whenever there is an exception (an error). Try to increment key's value. If there is an error (e.g. no key found), create the key and set value to 1.
@app.route('/', methods=['GET'])
def index():
    try:
        session['counter'] += 1
    except:
        session['counter'] = 1
    return render_template("index.html")

@app.route('/2', methods=['POST'])
def count2():
    session['counter'] += 1
    return redirect ('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect ('/')

app.run(debug=True)