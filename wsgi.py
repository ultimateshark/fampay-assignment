import os

from app import create_app

app = create_app(os.getenv("FLASK_ENV") or "prod")
if __name__ == "__main__":
    app.run(debug=True)