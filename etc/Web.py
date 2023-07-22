from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Simple Web App!"


@app.route('/about')
def about():
    return "This is a simple web app created with Python and Flask."


@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}! Welcome to the web app."


@app.route('/template')
def template_example():
    return render_template('template.html')


if __name__ == '__main__':
    app.run(debug=True)
