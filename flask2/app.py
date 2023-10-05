from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check-number', methods=['GET'])
def check_number():
    number = request.args.get('number')
    
    if not number.isdigit():
        result = 'Not an Integer'
    elif int(number) % 2 == 0:
        result = 'Even'
    else:
        result = 'Odd'

    return render_template('result.html', number = number, result = result)

if __name__ == '__main__':
    app.run(debug = True)
