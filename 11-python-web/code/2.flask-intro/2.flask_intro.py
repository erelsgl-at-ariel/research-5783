from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
        <h1>Hello World!!</h1>
        <a href="/about">about</a>
        '''

@app.route('/about')
def about():
    return '<h2>About</h2>'

if __name__ == '__main__':
    app.run(debug = True)
