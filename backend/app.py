from flask import Flask
from scanner import scanner_bp
from ssrf import ssrf_bp
from assistant import assistant_bp

app = Flask(__name__)

# Register Blueprints (modular API structure)
app.register_blueprint(scanner_bp, url_prefix="/scanner")
app.register_blueprint(ssrf_bp, url_prefix="/ssrf")
app.register_blueprint(assistant_bp, url_prefix="/assistant")

if __name__ == "__main__":
    app.run(debug=True)
