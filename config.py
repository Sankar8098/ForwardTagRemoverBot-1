import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    BOT_TOKEN = os.environ.get("BOT_TOKEN","6007679666:AAGj-MxoB8ethsDvVfyJf1Zi7hNwkf3Ll6c")
    SUPPORT = "https://t.me/Chatting_Spot"
    START_TEXT = """
Hi [{}](tg://user?id={}) 
I am A Forward Tag remover Bot.
Send /help to know more ©@SexyPiyush"""
    HELP_TEXT = "Forward Me A File,Video,Audio,Photo or Anything And \nI will Send You the File Back\n\n`How to Set Caption?`\nReply Caption to a File,Photo,Audio,Media"
