import os

class Config:
    # Load API keys from environment variables (more secure)
    GEMINI_API_KEY = os.getenv("AIzaSyA_cVwS9XqomAfh0jFJ2Kk1MBByGCOvPwY", "AIzaSyA_cVwS9XqomAfh0jFJ2Kk1MBByGCOvPwY")

    # Burp Suite API (if used)
    BURP_API_URL = "http://127.0.0.1:1337/v0.1/scan"

    # Security settings
    RATE_LIMIT_REQUESTS_PER_MIN = 10  # Example: 10 requests per minute

    # Database settings
    DB_URI = "sqlite:///../database/db.sqlite3"  # Change for PostgreSQL or MySQL if needed

# Initialize the config
config = Config()
