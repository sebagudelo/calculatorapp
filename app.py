from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

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
        # Get the expression from the request
        expression = request.json.get('expression', '')
        print(f"Received expression: {expression}")
        
        # Perform the calculation
        result = eval(expression)
        print(f"Calculated result: {result}")
        
        # Format the result
        if isinstance(result, (int, float)):
            formatted_result = str(result)
        
        # Get a random cat image from the API
        headers = {
            'x-api-key': 'DEMO-API-KEY'  # Optional: you can get a free API key from thecatapi.com
        }
        cat_response = requests.get('https://api.thecatapi.com/v1/images/search', headers=headers)
        print(f"Cat API Response: {cat_response.text}")  # Debug print
        
        cat_data = cat_response.json()
        cat_url = cat_data[0]['url']
        print(f"Cat URL: {cat_url}")  # Debug print
        
        return jsonify({
            'result': formatted_result,
            'cat_url': cat_url
        })
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'result': str(e)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port) 