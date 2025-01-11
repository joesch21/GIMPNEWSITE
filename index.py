from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is your Flask app running on Vercel!"

if __name__ == "__main__":
    app.run()
