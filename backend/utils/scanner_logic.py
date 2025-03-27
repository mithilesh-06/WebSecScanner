from flask import Blueprint, request, jsonify
from utils.scanner_logic import run_nuclei_scan, run_burp_scan, generate_dynamic_payloads, analyze_scan_results

scanner_bp = Blueprint("scanner", __name__)

@scanner_bp.route("/scan", methods=["POST"])
def scan():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL is required"}), 400

    # Generate attack payloads dynamically
    payloads = generate_dynamic_payloads(url)

    # Run both Nuclei and Burp Suite Scans
    nuclei_results = run_nuclei_scan(url)
    burp_results = run_burp_scan(url)

    # AI-Generated Security Report
    full_scan_data = f"Payloads:\n{payloads}\n\nNuclei:\n{nuclei_results}\n\nBurp:\n{burp_results}"
    ai_report = analyze_scan_results(full_scan_data)

    return jsonify({
        "generated_payloads": payloads,
        "nuclei_scan_results": nuclei_results,
        "burp_scan_results": burp_results,
        "ai_report": ai_report
    })
