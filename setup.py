import os
import subprocess
import sys


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


def main():
    print("Starting setup process...")
    
    # Ensure pip is installed and updated
    ensure_pip()

    # Install required packages
    required_packages = ["flask", "twilio"]
    for package in required_packages:
        install_package(package)

    # Check and create project structure
    check_and_create_structure()

    print("\nSetup complete! You can now run the project.")
    print("To start the web dashboard, navigate to 'app/' and run:")
    print("    python app.py")


if __name__ == "__main__":
    main()
