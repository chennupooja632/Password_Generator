from flask import Flask, render_template
import string
import random
app = Flask(__name__)

@app.route('/')

@app.route('/intro',methods = ['post','get'])
def index():
    return render_template('intro.html')

@app.route('/result',methods = ['POST','GET'])
def result():
    password_length = 12
    letters = string.ascii_letters
    digits = string.digits
    characters = string.punctuation
    total_char = letters+digits+characters
    first_char = random.choice(letters)
    password = first_char + ''.join([random.choice(total_char) for i in range(password_length-1)])

    return render_template('result.html',password = password)
if __name__ == "__main__":
    app.run(debug=True)