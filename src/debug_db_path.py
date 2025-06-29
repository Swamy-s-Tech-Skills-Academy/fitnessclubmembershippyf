# Debug database path and location
import os
from app import app
from models import db


def debug_database_path():
    with app.app_context():
        print("=== DATABASE PATH DEBUG ===")
        print(
            f"App config DATABASE_URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
        print(f"Current working directory: {os.getcwd()}")

        # Check if database file exists
        db_path = app.config['SQLALCHEMY_DATABASE_URI'].replace(
            'sqlite:///', '')
        abs_db_path = os.path.abspath(db_path)
        print(f"Database file path: {abs_db_path}")
        print(f"Database file exists: {os.path.exists(abs_db_path)}")

        if os.path.exists(abs_db_path):
            file_size = os.path.getsize(abs_db_path)
            print(f"Database file size: {file_size} bytes")


if __name__ == "__main__":
    debug_database_path()
