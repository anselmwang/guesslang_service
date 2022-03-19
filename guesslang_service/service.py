import guesslang
from flask import Flask, request
from flask_cors import CORS

####################################################################################
# config
####################################################################################
PORT = 5000
HOST = '127.0.0.1'

app = Flask(__name__)
####################################################################################
# Cors
####################################################################################
# Allows access to fetch at 'http://localhost:5000/' from origin 'app://obsidian.md'
obsidian_origin = "app://obsidian.md"
cors = CORS(app, origins=obsidian_origin)
app.config['CORS_HEADERS'] = 'Content-Type'

####################################################################################
# Routers
####################################################################################
'''Return a list of all detected plugins'''

@app.route('/', methods=['GET'])
def root():
    return {
        'scripts': [
                f'http://{HOST}:{PORT}/hello'
            ]
    }

@app.route('/prob', methods=['POST'])
def run():
    code = request.json['code']
    return {
        "scores": guess.probabilities(code)
    }

guess = guesslang.Guess()
def main():
    app.run(port=PORT, host=HOST)
    
if __name__ == '__main__':
    main()
