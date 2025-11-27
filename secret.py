import os
from dotenv import load_dotenv

# Load .env file if it exists (for local testing)
load_dotenv()

# Read from Environment Variables (for Render)
# If not found in env, it returns None or the second argument
EMAIL = os.getenv("EMAIL")
SECRET = os.getenv("SECRET")
AIPIPE_TOKEN = os.getenv("AIPIPE_TOKEN")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Simple check to ensure they exist
if not all([EMAIL, SECRET, AIPIPE_TOKEN]):
    print("WARNING: One or more secrets are missing from Environment Variables!")
