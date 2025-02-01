from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Add these headers to allow access
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Print the received data for debugging
        print("Received data:", request.json)
        
        expression = request.json.get('expression', '')
        print("Expression to evaluate:", expression)
        
        # Simple test calculation
        result = eval(expression)
        print("Calculated result:", result)
        
        # Fetch a random cat image
        cat_response = requests.get('https://api.thecatapi.com/v1/images/search')
        cat_data = cat_response.json()
        cat_url = cat_data[0]['url']
        
        return jsonify({
            'result': str(result),
            'cat_url': cat_url
        })
    except Exception as e:
        print("Error occurred:", str(e))
        return jsonify({'result': f'Error: {str(e)}'})

app.debug = True

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)