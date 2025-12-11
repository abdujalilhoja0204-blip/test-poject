from flask import Flask
app = Flask(__name__)

@app.get("/")
def home():
    return "CI/CD with Docker works!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
