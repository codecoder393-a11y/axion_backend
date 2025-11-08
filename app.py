from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

# Initialize Flask app with CORS
CORS(app)

@app.route("/")
def home():
    return jsonify({"status": "healthy"})

# This is for Vercel serverless deployment
def handler(request):
    return app(request)

if __name__ == "__main__":
    app.run()