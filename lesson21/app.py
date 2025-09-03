from flask import Flask, render_template
from dotenv import load_dotenv
import os

# 載入環境變數
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
