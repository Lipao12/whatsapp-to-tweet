import os
from dotenv import load_dotenv
load_dotenv()

print(f"My secret .env: {os.getenv('SECRET')}")