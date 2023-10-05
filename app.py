# wsgi.py

from main import app  # Replace with your actual Flask app instance

if __name__ == "__main__":
    app.run(threaded=True)
