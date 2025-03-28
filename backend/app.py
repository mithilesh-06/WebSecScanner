from flask import Flask, render_template

app = Flask(__name__, static_folder="../frontend/static", template_folder="../frontend")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scanner")
def scanner():
    return render_template("scanner.html")

@app.route("/ssrf")
def ssrf():
    return render_template("ssrf.html")

if __name__ == "__main__":
    app.run(debug=True)
