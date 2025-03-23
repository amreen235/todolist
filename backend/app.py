from flask import Flask
from flask_cors import CORS
from models import db
from config import SQLALCHEMY_DATABASE_URI
from routes.task_routes import task_bp

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db.init_app(app)

app.register_blueprint(task_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
