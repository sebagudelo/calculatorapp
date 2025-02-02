from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        expression = request.json.get('expression', '')
        result = eval(expression)
        return jsonify({
            'result': str(result),
            'cat_url': 'https://placekitten.com/200/300'  # Static cat image for testing
        })
    except Exception as e:
        return jsonify({'result': f'Error: {str(e)}'})

# Add this for Vercel
@app.route('/api/health')
def health_check():
    return jsonify({'status': 'ok'})