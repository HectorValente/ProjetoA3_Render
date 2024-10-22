from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return "Olá Mundo!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)