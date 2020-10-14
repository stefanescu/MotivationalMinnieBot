from uuid import uuid4
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
import requests, bs4, logging
from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
updater = Updater(token='nonono')

dispatcher = updater.dispatcher

def getInsult():
    page = requests.get('http://www.insultgenerator.org/')
    soup = bs4.BeautifulSoup(page.text, "html.parser")
    text = soup.select('.wrap br br')
    return text[0].getText()

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="RudeDude reporting for duty! Use me inline with people you despise.")

def rudeResponse(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=getInsult())

def inlineInsult(bot, update):
    #query = update.inline_query.query
    results = list()
    for i in xrange(3):
        text = getInsult()
        results.append(InlineQueryResultArticle(id=uuid4(), title="#" + str(i+1), input_message_content=InputTextMessageContent(text), description=text))

    update.inline_query.answer(results)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

rude_handler = MessageHandler([Filters.text], rudeResponse)
dispatcher.add_handler(rude_handler)

inline_handler = InlineQueryHandler(inlineInsult)
dispatcher.add_handler(inline_handler)

updater.start_polling()

updater.idle()
