# 🔍 Advanced Web Security Suite

This project is a **fully automated** web security tool that includes:  
✔ **Website Vulnerability Scanner** (Detects XSS, SQLi, Open Redirects, SSRF).  
✔ **SSRF Testing Suite** (Automates SSRF detection with dynamic payloads).  
✔ **AI-Powered Bug Bounty Assistant** (Uses Google Gemini API to provide security insights).  

## 🚀 Features
- AI-powered vulnerability scanning with dynamic payload generation.  
- Fully automated SSRF testing with Burp Collaborator-style detection.  
- Bug bounty assistant providing **real-time hacking tips** based on target tech stacks.  

---

## 📂 Folder Structure

project-root/ │── backend/ # Backend API (Flask) │ │── app.py # Main Flask app │ │── scanner.py # Vulnerability scanner API │ │── ssrf.py # SSRF testing API │ │── assistant.py # AI assistant API │ │── config.py # Configurations (API keys, rate limits) │ └── utils/ │ │── scanner_logic.py # Scanner logic & automation │ └── security.py # Security functions (rate-limiting, validation) │ │── database/ # Database models │ │── models.py # SQLAlchemy models │ └── db.sqlite3 # SQLite database (generated automatically) │ │── frontend/ # Frontend UI │ │── index.html # Main landing page │ │── scanner.html # Vulnerability Scanner UI │ │── ssrf.html # SSRF Testing UI │ │── assistant.html # AI Bug Bounty Assistant UI │ └── css/ │ └── styles.css # Custom styles │ │── tests/ # Automated tests │ │── test_scanner.py # Scanner API tests │ │── test_ssrf.py # SSRF tests │ └── test_assistant.py # AI assistant tests │ │── requirements.txt # Python dependencies │── .gitignore # Ignore unnecessary files └── README.md # Project documentation