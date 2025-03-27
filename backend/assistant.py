from flask import Blueprint, request, jsonify
import google.generativeai as genai

assistant_bp = Blueprint("assistant", __name__)

# Configure Google Gemini API
genai.configure(api_key="AIzaSyA_cVwS9XqomAfh0jFJ2Kk1MBByGCOvPwY")

@assistant_bp.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question")

    if not question:
        return jsonify({"error": "Question required"}), 400

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question)

    return jsonify({"answer": response.text})
