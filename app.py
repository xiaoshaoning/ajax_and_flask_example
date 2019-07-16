from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def do_sum():
    num_1 = request.form['num1']
    num_2 = request.form['num2']
    output = str(int(num_1) * int(num_2))
    if num_1 and num_2:
            return jsonify({'output':'Result: ' + output})
    return jsonify({'error':'Missing data!'})

if __name__ == '__main__':
    app.run()
