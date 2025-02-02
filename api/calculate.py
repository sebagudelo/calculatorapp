from flask import Flask, request, jsonify
from flask import render_template

app = Flask(__name__, template_folder='../templates')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/api/calculate', methods=['POST'])
def calculate():
    try:
        expression = request.json.get('expression', '')
        result = eval(expression)
        return jsonify({
            'result': str(result),
            'cat_url': 'https://placekitten.com/200/300'
        })
    except Exception as e:
        return jsonify({'result': f'Error: {str(e)}'}) 