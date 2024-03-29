from flask import Flask, render_template
app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greetings/')
def greetings():
    return render_template('greetings.html')
app.run(host='0.0.0.0', debug=True)