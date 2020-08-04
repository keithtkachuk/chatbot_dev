from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", read_only=True,
									storage_adapter='chatterbot.storage.SQLStorageAdapter',
    								preprocessors=[
        							'chatterbot.preprocessors.clean_whitespace',
        							'chatterbot.preprocessors.unescape_html',
        							'chatterbot.preprocessors.convert_to_ascii'
    								])


trainer = ListTrainer(english_bot)

trainer.train([
    'How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])

exceptionList = ['HAVE A NICE DAY','BYE','GOOD BYE','GOOD BYE !']

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")

def get_bot_response():
	while True:
		try:	
			userText = request.args.get('msg')
			if userText.upper() in exceptionList:
				break
			else:
				return str(english_bot.get_response(userText))
		except(KeyboardInterrupt, EOFError, SystemExit):
			break
	return ('Have a nice day !')

	sys.exit()
		
if __name__ == "__main__":
    app.run()
