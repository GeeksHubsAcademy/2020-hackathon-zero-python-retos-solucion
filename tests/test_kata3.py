import pytest

from kata3.bot import start, help, mayus, alreves

class Message():
    text = ''

    def reply_text(self, palabra):
        return palabra

class Update:
    message = Message()

class Context:
    args = []

def test_command_start():
    update = Update()
    assert(start(update, '') == 'Hola, Geeks!')

def test_command_help():
    update = Update()
    assert(help(update, '') == 'Ayudame!')

def test_command_mayus():
    update = Update()
    context = Context()
    context.args = ['hola']

    assert(mayus(update, context) == 'HOLA')

def test_command_alreves():
    update = Update()
    update.message.text = 'hola'

    assert(alreves(update, '') == 'aloh')