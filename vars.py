#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "27400172"))
API_HASH = environ.get("API_HASH", "56d0a75c5f9a9de6beb5452aa63c2d36")
BOT_TOKEN = environ.get("BOT_TOKEN", "8396814092:AAHtUGEPciF5LdiCo572-TczY3EZwx0Otis")

OWNER = int(environ.get("OWNER", "7540570087"))
CREDIT = environ.get("CREDIT", "")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7540570087,7061670859').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7540570087,7061670859').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set


