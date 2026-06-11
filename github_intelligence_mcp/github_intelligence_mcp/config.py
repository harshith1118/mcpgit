import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
APP_NAME = "github-intelligence"
