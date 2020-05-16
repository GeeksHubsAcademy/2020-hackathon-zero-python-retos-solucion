# 2020-hackathon-python-retos-soluciones

<p align="center">
    <img src="https://github.com/GeeksHubsAcademy/2020-geekshubs-media/blob/master/image/logo.png" >	
</p>


<p align="center">
    <img src="https://github.com/GeeksHubsAcademy/2020-geekshubs-media/blob/master/image/2020-hackathon.png" >	
</p>

[![Build Status](https://travis-ci.com/GeeksHubsAcademy/-2020-hackathon-zero-python-retos-soluci-n.svg?branch=master)](https://travis-ci.com/GeeksHubsAcademy/-2020-hackathon-zero-python-retos-soluci-n)

Kata 1
```
from random import randint

options = ["Piedra", "Papel", "Tijeras"]

def quienGana(player, ai):
    player = player.lower()
    ai = ai.lower()
    
    if player == ai:
        return 'Empate!'
    elif player == "piedra" and ai == "tijeras":
        return "Ganaste!"
    elif player == "papel" and ai == "piedra":
        return "Ganaste!"
    elif player == "tijeras" and ai == "papel":
        return "Ganaste!"

    return "Perdiste!"
        
def Game():
    player = input("¿Piedra, Papel o Tijeras?")
    print("Elegiste: " + player)

    ai = options[randint(0,2)]
    print("AI eligio: " + ai)

    winner = quienGana(player, ai)

    print("Por lo tanto, haz: "  + winner )
```

kata 2
```
#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''

    for i in range(passLen):
        password += random.choice(characters)

    return password
```

Kata 3
```
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start(update, context):
    """Envia un mensaje cuando se emita el comando /start."""
    return update.message.reply_text('Hola, Geeks!')


def help(update, context):
    """Envia un mensaje cuando se emita el comando /help."""
    return update.message.reply_text('Ayudame!')

def mayus(update, context):
        palabra = context.args[0].upper()
        return update.message.reply_text(palabra)

def alreves(update, context):
    """Repite el mensaje del usuario."""
    texto = update.message.text[::-1]
    return update.message.reply_text(texto)

def error(update, context):
    """Envia los errores por consola"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Inicio del Bot"""

    #Colocamos el Token creado por FatherBot
    updater = Updater("****AQUí LA KEY****", use_context=True)

    # Es el Registro de Comandos
    dp = updater.dispatcher

    # Añadimos a la lista de Registro todos los comandos con su función
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("mayus", mayus))

    # Este comando es un Trigger.
    dp.add_handler(MessageHandler(Filters.text, alreves))


    # Y este espera al error
    dp.add_error_handler(error)

    # Lanzamos el Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
```

kata4
```
import pygame, sys, time, random
from pygame.locals import *

#pygame.init()
#play_surface = pygame.display.set_mode((500, 500))
#fps = pygame.time.Clock()

class Snake():
    position = [100,50]
    body = [[100,50], [90,50],[80,50]]
    direction = "RIGHT"
    change = direction

    def controller(self, event, pygame):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.change = "RIGHT"
            if event.key == pygame.K_LEFT:
                self.change = "LEFT"
            if event.key == pygame.K_UP:
                self.change = "UP"
            if event.key == pygame.K_DOWN:
                self.change = "DOWN"

    def changeDirection(self):
        if self.change == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"
        if self.change == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        if self.change == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        if self.change == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"

        if self.direction == "RIGHT":
            self.position[0] += 10
        if self.direction == "LEFT":
            self.position[0] -= 10
        if self.direction == "UP":
            self.position[1] -= 10
        if self.direction == "DOWN":
            self.position[1] += 10

        self.body.insert(0, list(self.position))

class Game():
    run = True
    food_pos = 0
    score = 0

    def __init__(self):
        self.food_spawn()

    def exit(self, event, pygame):
        if event.type == pygame.QUIT:
            self.run = False

    def food_spawn(self):
        self.food_pos = [random.randint(0,49)*10, random.randint(0,49)*10]

    def eat(self, snake):
        if snake.position == self.food_pos:
            self.food_spawn()
            self.score += 1
        else:
            snake.body.pop()

    def dead(self, snake):
        if snake.position[0] >= 500 or snake.position[0] <=0:
            print(f"Game Over! Score: {self.score})")
            self.run = False
            
        if snake.position[1] >= 500 or snake.position[1] <=0:
            print(f"Game Over! Score: {self.score})")
            self.run = False

        if snake.position in snake.body[1:]:
            print(f"Game Over! Score: {self.score})")
            self.run = False

def main():
    snake = Snake()
    game = Game()

    while game.run:
        for event in pygame.event.get():
            game.exit(event, pygame)
            snake.controller(event, pygame)

        snake.changeDirection()

        game.eat(snake)

        # Dibujar Snake
        play_surface.fill((0,0,0))
        for pos in snake.body:
            pygame.draw.rect(play_surface, (200,200,200), pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(play_surface, (255,160,60), pygame.Rect(game.food_pos[0], game.food_pos[1], 10, 10))

        game.dead(snake)

        pygame.display.flip()
        fps.tick(10)

#main()
#pygame.quit()
```

# Gracias a todos por participar!!!!

![](https://github.com/GeeksHubsAcademy/2020-hackathon-zero-python-retos-solucion/blob/master/epic.gif)

# Test Passed - Oráculo

![](https://github.com/GeeksHubsAcademy/2020-hackathon-zero-python-retos-solucion/blob/master/test.png)
![](https://github.com/GeeksHubsAcademy/2020-hackathon-zero-python-retos-solucion/blob/master/Oraculo.png)

## Referencias


* [Tutorial - Testing Automatizado](https://github.com/GeeksHubsAcademy/2020-js-vanilla-testing-FFFF/blob/master/README.md)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Telegram-Bot](https://pypi.org/project/python-telegram-bot/)
* [Pygame](https://pypi.org/project/pygame/)
* [Fundamentos Python](https://github.com/GeeksHubsAcademy/FundamentosPython)
* [Telegram Bot](https://github.com/GeeksHubsAcademy/TelegramBot)
* [Pong - PyGame](https://github.com/GeeksHubsAcademy/PongPygame)
* [Principal](https://github.com/GeeksHubsAcademy/2020-hackathon-zero-python-retos-main)
