import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

def generate_report(scan_results):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Generate a security report based on: {scan_results}")
    return response.text
