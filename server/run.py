from flask import Flask

app = Flask(__name__)


@app.route('/name')
def name():
    return {'name': 'Kieran Dee'}


if __name__ == '__main__':
    app.run()
