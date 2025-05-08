from flask import Flask, render_template
from models import Contact
app = Flask(__name__)

def 



@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
