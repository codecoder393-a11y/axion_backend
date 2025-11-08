from flask_cors import CORS

def configure_cors(app):
    CORS(app, resources={
        r"/*": {
            "origins": [
                "https://axion-digitaverse-7dvnllt3b-codes-projects-57d381b5.vercel.app",
                "http://localhost:5173",  # Local development
                "http://localhost:3000",   # Alternative local port
                "https://axion-digitaverse.vercel.app"  # Production frontend
            ],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization", "Accept"],
            "supports_credentials": True,
            "expose_headers": ["Content-Type", "Authorization"],
            "max_age": 600
        }
    })
