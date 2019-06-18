from flask import Flask, request, redirect
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['POST'])
def table_name():
    formName = list(request.form.keys())
    print(request)
    print(formName)
    return "Received table name"

if __name__ == "__main__":
    app.run("0.0.0.0", "5000")