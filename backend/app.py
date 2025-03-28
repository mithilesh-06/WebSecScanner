from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/assistant/ask', methods=['POST'])
def assistant():
    try:
        # Ensure request data is JSON
        if not request.is_json:
            return jsonify({"error": "Invalid JSON"}), 400

        data = request.get_json()
        question = data.get('question', '')

        # Simulating AI response
        response = {"answer": f"AI Response for: {question}"}

        return jsonify(response), 200  # Ensure JSON response
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return proper JSON error

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)  # Make sure it runs properly
