import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7438164515:AAGZankxbqJLVOfn7fyXHfP_0jQtGI-fDmA")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21551881"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6e83e9e1aee5accd4868dc29aa59ebaa")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://david:surya@cluster0.s7o0tyw.mongodb.net/")
