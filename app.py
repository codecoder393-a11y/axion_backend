from flask import Flask, request, jsonify  # type: ignore
import requests  # type: ignore
from flask_cors import CORS  # type: ignore
from axion_chain import Blockchain, generate_key_pair
from axion_ai import AxionAI
from axion_vm import AxionVM
from axion_blockchain.p2p import PeerNetwork
from axion_blockchain.file_storage import FileStorage
import os
import time
import sys
import io
import shutil
import random
import uuid
import json
import datetime

app = Flask(__name__)
CORS(app)

# --- ECONOMIC CONSTANTS ---
GAS_FEE = 0.01
SUPERUSER_BALANCE = 1_000_000.0

# --- INITIALIZE CORE COMPONENTS ---
blockchain = Blockchain()
axion_ai = AxionAI(blockchain)
axion_vm = AxionVM(blockchain)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
PROPERTY_UPLOADS = os.path.join(UPLOAD_FOLDER, "properties")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROPERTY_UPLOADS, exist_ok=True)

@app.route("/")
def home():
    return jsonify({"status": "healthy"})

# Import all the routes after app is defined
from main import *

if __name__ == "__main__":
    app.run()