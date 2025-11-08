from flask import Flask, request, jsonify
from blockchain import Blockchain
import json
from flask_cors import CORS  # type: ignore
import os
import requests  # type: ignore
from axion_ai import AxionAI
from cors_config import configure_cors  # Import our CORS configuration

# Initialize Flask app
app = Flask(__name__)
configure_cors(app)  # Apply our CORS configuration
configure_cors(app)  # Apply our CORS configuration
