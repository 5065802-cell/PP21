from flask import Flask, make_response

app = Flask(__name__)

@app.route("/")
def home():
    resp = make_response("<h2>Security Headers Applied</h2><p>Check Network tab in DevTools.</p>")
    resp.headers["X-Frame-Options"] = "DENY"
    resp.headers["Content-Security-Policy"] = "default-src 'self'"
    return resp

if __name__ == "__main__":
    app.run(debug=True)
