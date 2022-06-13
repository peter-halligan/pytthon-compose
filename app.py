from flask import Flask
from flask import request
import os
from pathlib import Path

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return 'Hello World!'
    
@app.route('/1')
def secret1():
    return f'{os.environ.get("SECRET_HARDCODED")} SECRET_HARDCODED'

@app.route('/2')
def secret2():
    return f'{os.environ.get("SECRET_BASH_WRAPPER")} SECRET_BASH_WRAPPER'

@app.route('/3')
def secret3():
    return f'{os.environ.get("SECRET_ENV_FILE")} SECRET_ENV_FILE'

@app.route('/4')
def secret4():
    p = Path('/run/secrets/SECRET_SECRETS_FILE')
    password = p.read_text()
    return f'{password} code change to read from SECRETS_FILE'

@app.route('/4')
def secret4():
    p = Path('/run/secrets/SECRET_SECRETS_FILE')
    password = p.read_text()
    return f'{password} code change to read from SECRETS_FILE'

@app.route('/5')
def secret5():
    return f'{os.environ.get("SECRET_SECRETS_FILE")} code change to read from SECRETS_FILE'   

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
    