import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


class Colors:
    WARNING = '\033[93m'
    BOLD = '\033[1m'
    GREEN = '\033[92m'
    ERROR = '\033[91m'
    BLUE = '\033[94m'
    BLACK = '\033[90m'
