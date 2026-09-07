import requests
import os

TARGET_URL = os.getenv("TARGET_URL", "https://google.com")

def check_health():
    try:
        response = requests.get(TARGET_URL, timeout=5)

        return {
            "status": "healthy",
            "target": TARGET_URL,
            "status_code": response.status_code
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "target": TARGET_URL,
            "error": str(e)
        }