from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder="../frontend", static_folder="../frontend/static")

# ✅ Fix 1: Add a homepage route to serve index.html
@app.route('/')
def home():
    return render_template('index.html')  # Ensure index.html exists in frontend/

# ✅ Fix 2: Fix /assistant/ask route (Allow GET for testing)
@app.route('/assistant/ask', methods=['GET', 'POST'])
def assistant():
    try:
        if request.method == 'GET':
            return jsonify({"message": "Use POST to send a question."})

        data = request.json  # Ensure it's JSON
        question = data.get('question', '')

        # Simulating AI response
        response = {"answer": f"AI Response for: {question}"}
        return jsonify(response)  # Ensure returning JSON

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return proper JSON error

if __name__ == '__main__':
    app.run(debug=True)
