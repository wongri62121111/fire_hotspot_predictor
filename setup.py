import os
import subprocess
import sys
import webbrowser
import threading
import smtplib

def install_requirements():
    """
    Installs all Python packages listed in requirements.txt.
    """
    requirements_file = "requirements.txt"
    if not os.path.exists(requirements_file):
        print(f"Error: {requirements_file} not found.")
        sys.exit(1)

    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
        print(f"Installed all requirements from {requirements_file} successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to install requirements from {requirements_file}. Please check the file and your pip setup.")
        sys.exit(1)


def install_package(package_name):
    """
    Installs a Python package using pip.
    Args:
        package_name (str): The name of the package to install.
    """
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"Installed {package_name} successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package_name}. Please check your internet connection or pip setup.")
        sys.exit(1)


def ensure_pip():
    """
    Ensures that pip is installed and upgraded.
    """
    try:
        subprocess.check_call([sys.executable, "-m", "ensurepip"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        print("Pip is installed and upgraded.")
    except subprocess.CalledProcessError:
        print("Failed to install or upgrade pip. Please check your Python installation.")
        sys.exit(1)


def check_and_create_structure():
    """
    Ensures the project directory structure exists and creates missing parts.
    """
    structure = {
        "modules": ["irregularity_detector.py", "notification_alert.py", "sensor_logger.py"],
        "data": ["wildfire_sensors.csv"],
        "app/templates": ["index.html"],
        "app/static": ["style.css"],
    }

    for folder, files in structure.items():
        os.makedirs(folder, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder, file)
            if not os.path.exists(file_path):
                open(file_path, "w").close()  # Create an empty file
                print(f"Created missing file: {file_path}")
    print("Project structure verified and missing files created.")

def start_flask_app():
    """
    Starts the Flask web application in a separate thread.
    """
    app_directory = os.path.abspath("app")
    if not os.path.exists(os.path.join(app_directory, "app.py")):
        print("Error: app.py not found in the 'app/' directory.")
        sys.exit(1)

    print("Starting Flask application...")
    os.chdir(app_directory)
    try:
        subprocess.check_call([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("Flask application stopped.")


def open_browser():
    """
    Opens the default web browser to the Flask app's URL.
    """
    url = "http://127.0.0.1:5000"
    print(f"Opening browser at {url}...")
    webbrowser.open(url)

def main():
    print("Starting setup process...")

    # Ensure pip is installed and updated
    ensure_pip()

    # Install dependencies from requirements.txt
    install_requirements()

    # Check and create project structure
    check_and_create_structure()

    # Start Flask app and open browser
    threading.Thread(target=open_browser, daemon=True).start()  # Open browser in a separate thread
    start_flask_app()

    print("\nSetup complete! The web dashboard should now be running.")


if __name__ == "__main__":
    main()