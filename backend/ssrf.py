from flask import Blueprint, request, jsonify
import requests
from utils.report_generator import generate_report

ssrf_bp = Blueprint("ssrf", __name__)

@ssrf_bp.route("/test", methods=["POST"])
def ssrf_test():
    data = request.json
    target_url = data.get("url")

    if not target_url:
        return jsonify({"error": "Target URL required"}), 400

    # User-defined SSRF Payload Testing
    test_payload = request.json.get("payload", "")
    response = requests.get(target_url + "?url=" + test_payload, timeout=5)

    results = {"payload": test_payload, "status_code": response.status_code}

    # AI-Generated Report
    ai_report = generate_report(results)

    return jsonify({"results": results, "ai_report": ai_report})
