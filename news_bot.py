import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

API_KEY = "9804a660b39f49f89ecd04738c67ace9"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to the News Bot! Use /news to get the latest headlines.")

def get_news(update: Update, context: CallbackContext) -> None:
    news_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
    
    response = requests.get(news_url)
    news_data = response.json()

    articles = news_data.get("articles", [])
    news_text = "\n\n".join([f"{article['title']}\n{article['url']}" for article in articles])

    update.message.reply_text(news_text)

def main():
    updater = Updater(token="6630793232:AAGcPAr9kKH0wOASfqnr0pXB_5Clt6LmqXo", use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("news", get_news))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
