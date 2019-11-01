from flask import Flask
from flask import request
import requests
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello!"

@app.route('/sendpost')
def post():
    u = request.args.get('url')
    p = request.args.get('payload')
    if None in (u,p):
        return "u: {} p: {}".format(u,p)

    PARAMS = {'payload':p}
    r = requests.post(url = u, data = PARAMS)
    return r.content

@app.route('/testendpoint', methods=['POST'])
#http://127.0.0.1:5000/sendpost?url=http://localhost:5000/testendpoint&payload=testo
def testendpoint():
    p = request.form['payload']
    return p

if __name__ == '__main__':
    app.run()