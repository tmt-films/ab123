import os
from dotenv import load_dotenv

load_dotenv("./.env")


class Config:
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7917525595:AAHBFYfJnHEKTWUEXTHjGWlm5yfDAztx83k")
  BOT_NAME = os.environ.get("BOT_NAME", "mrina")

  API_ID = int(os.environ.get("API_ID", "25120562"))
  API_HASH = os.environ.get("API_HASH", "0bd8eb78385a059f64f6032ebefc4615")

  DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://mrina:mrina@cluster0.xy5zmcd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  SESSION_NAME = os.environ.get("DATABASE_NAME", "mrina")

  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1002522178088))
  SUDO_USERS = [int(user) for user in (os.environ.get("SUDO_USERS","7769775189")).split()]
  SUPPORT_CHAT_URL = os.environ.get("SUPPORT_CHAT_URL", "https://t.me/Queens_Supports")
