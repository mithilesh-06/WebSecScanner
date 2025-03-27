from flask import Blueprint, request, jsonify
import subprocess
from utils.report_generator import generate_report

scanner_bp = Blueprint("scanner", __name__)

@scanner_bp.route("/scan", methods=["POST"])
def scan():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL is required"}), 400

    # Run Nuclei Scanner
    scan_result = subprocess.getoutput(f"nuclei -u {url}")

    # AI-Generated Report
    ai_report = generate_report(scan_result)

    return jsonify({"scan_result": scan_result, "ai_report": ai_report})
