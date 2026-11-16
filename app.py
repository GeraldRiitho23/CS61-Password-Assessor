from flask import Flask, request, jsonify
from logic import evaluate_password

app = Flask(__name__)

@app.route('/assess', methods=['POST'])
def assess_password():
    data = request.get_json()
    
    if not data or 'password' not in data:
        return jsonify({"error": "Missing password field"}), 400
        
    password = data['password']
    
    # Call Lorcan's logic function
    score, rules_passed, feedback = evaluate_password(password)
    
    # Return the JSON response
    return jsonify({
        "score": score,
        "rules_passed": rules_passed,
        "feedback": feedback
    }), 200

if __name__ == '__main__':
    app.run(port=5001)
