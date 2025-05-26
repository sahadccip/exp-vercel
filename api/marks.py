from flask import Flask, request, jsonify
import json
import os

# 1. Initialize Flask app FIRST
app = Flask(__name__)

# 2. Load data file
def load_marks_data():
    try:
        json_path = os.path.join(os.path.dirname(__file__), '..', 'q-vercel-python.json')
        with open(json_path) as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

# 3. Define your API route
@app.route('/api', methods=['GET'])
def api_handler():
    marks_data = load_marks_data()
    names = request.args.getlist('name')
    result = []
    
    for name in names:
        found = next(
            (item for item in marks_data 
             if str(item.get('name', '')).lower() == name.lower()),
            None
        )
        result.append(found['marks'] if found else None)
    
    return jsonify({"marks": result})

# 4. Add root route for testing
@app.route('/')
def home():
    return "Flask server is running. Access API at /api?name=TkErBC"

# 5. CORS configuration
@app.after_request
def add_cors(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# 6. Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)