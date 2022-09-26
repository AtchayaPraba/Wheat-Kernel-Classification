import sys
from flask import Flask
from wheat.logger import logging
from wheat.exception import WheatException

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

def CICI_pipeline ():
    try:
        raise Exception("Testing custome exception")
    except Exception as e:
        wheat = WheatException(e,sys)
        logging.info(wheat.error_message)
    # logging.info("Testing logging module")
    return ('Check for CI/CD pipeline. Check for changes in CI/CD pipeline')

if __name__ == '__main__':
    app.run(debug=True)

# python app.py