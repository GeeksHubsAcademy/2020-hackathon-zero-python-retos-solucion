def start(update, context):
    return update.message.reply_text('Hola')

class Message():
    text = ''

    def reply_text(self, text):
        return text

class Update:
    message = Message()

class Context:
    args = []


update = Update()
text = start(update, '')

print(text == 'Hola')