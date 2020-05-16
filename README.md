# 2020-hackathon-python-retos

<p align="center">
    <img src="https://github.com/GeeksHubsAcademy/2020-geekshubs-media/blob/master/image/logo.png" >	
</p>


```

El modus operandi de trabajo es el siguiente:

Debes 'Forkear' el proyecto a tu cuenta de Github.

Dos posibilidades de desarrollo :
    - Puedes hacer PR's ilimitadas e ir validando poco a poco la solución contra nuestro respositorio con CI.
    - Puedes trabajar en local y subir la solución a tu 'Fork', luego nos haces una PR a nuestro repositorio.

Cuando se envíe la PR, indica la Kata actual en el nombre de la PR.
También puedes añadir un comentario para dar cualquier tipo de feedback.

Una vez envíes la primera PR, todas la siguientes se añaden consecutivamente en la misma.
Recuerda que nosotros no vamos aceptarla hasta que todos los Tests esten en verde.


En caso de duda, revisa en el apartado de 'Referencias'.
Hay una guía que donde explica todos los pasos.

No se aceptarán PR's validas que añadan cualquier tipo de carpeta con assets que no sean los que vienen en el repo.
No se aceptarán PR's validas que cambien el comportamiento de la estructura del proyecto.

En caso de empate, atenderemos al orden de cola de ejecución del cliente de la integración continua.





Este repositorio cumple con una solución 'Python' que se abre con 'Visual Studio Code'.
Se han añadido los ficheros raiz del proyecto para su fácil uso en local.
	- .vscode
	- main.code-workspace
	
Una vez forkeado, puedes clonarlo/descargarlo en tu local.
Abrimos Visual Studio Code
    - File
    - Open Workspace

Seleccionar fichero
    - main.code-workspace


A continuación se describe la estructura de la paquetería :

Carpeta 'src'
    - Contiene los diferentes retos.
    - En cada carpeta se presenta un fichero con métodos vacíos que hay que implementar.

Carpeta 'test'
    - Contiene la suite de test que ejecuta el código de los métodos de la carpeta 'src'.

Fichero .travis.yml
    - Define una configuración con pseudo-código que permite lanzar los test en un
      entorno pre-configurado con Integración Continua o también llamado 'CI'.
    
Fichero setup.py
    - Fichero de configuración.


Para instalar Python en Visual Studio Code
    - Control+Shift+X
    - En el buscador ponemos el id 'ms-python.python', a la derecha del icono - Install



Definimos los siguientes retos:

Reto 1 - Piedra, Papel o Tijera ?

Se atiente a un pequeño juego donde el Player-1 escoge una acción [Piedra - Papel - Tijera].
Una pequeña IA contesta al player-1 con una elección aleatoria.
Tras la elección de ambos, se dicta el resultado del Player-1.
Ganador, Perdedor o Empate ???

Test Suite

def test_no_sensible_minusculas():
    assert(quienGana('Piedra', 'Papel') == 'Perdiste!')

def test_piedra_vs_piedra():
	assert(quienGana('Piedra', 'Piedra') == 'Empate!')

def test_papel_vs_papel():
	assert(quienGana('Papel', 'Papel') == 'Empate!')

def test_tijeras_vs_tijeras():
	assert(quienGana('Tijeras', 'Tijeras') == 'Empate!')

def test_piedra_vs_papel():
	assert(quienGana('Piedra', 'Papel') == 'Perdiste!')

def test_papel_vs_tijeras():
	assert(quienGana('Papel', 'Tijeras') == 'Perdiste!')

def test_tijeras_vs_piedra():
	assert(quienGana('Tijeras', 'Piedra') == 'Perdiste!')

def test_piedra_vs_tijeras():
	assert(quienGana('Piedra', 'Tijeras') == 'Ganaste!')

def test_papel_vs_piedra():
	assert(quienGana('Papel', 'Piedra') == 'Ganaste!')

def test_tijeras_vs_papel():
	assert(quienGana('Tijeras', 'Papel') == 'Ganaste!')


Dependencias en local por terminal
 - pip install -e .




Reto 2 - Random Password Generator

Pequeña aplicación que permite generar aleatoriamente un token 'cifrado'.
Nuestro James Bone de l'horta necesita tu ayuda!!!


Test Suite

def test_longitud_15():
	assert(len(RandomPasswordGenerator(15)) == 15)

def test_longitud_10():
	assert(len(RandomPasswordGenerator(10)) == 10)

def test_longitud_8():
	assert(len(RandomPasswordGenerator(8)) == 8)

def test_contraseña_contiene_letras():
	assert(chr in RandomPasswordGenerator(15) for chr in string.ascii_letters)

def test_contraseña_contiene_numeros():
	assert(chr in RandomPasswordGenerator(15) for chr in string.digits)

def test_contraseña_contiene_caracteres_especiales():
	assert(chr in RandomPasswordGenerator(15) for chr in string.punctuation)
    
def test_contraseña_contiene_letras():
	characters = string.ascii_letters + string.digits + string.punctuation
	assert(chr in RandomPasswordGenerator(15) for chr in characters)

def test_contraseña_compleja():
	characters = string.ascii_letters + string.digits + string.punctuation
	assert(chr in RandomPasswordGenerator(15) for chr in characters)

Dependencias en local por terminal
 - pip install -e .




Reto 3 - Tu primer Bot

A través de una mensajería bidireccional, se intercambian mensajes con un bot de manera estática.
Para ello se define un patrón comander que mapea lo mensajes [start - help - mayus].
A cada acción, tenemos una respuesta.


Test Suite

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


Dependencias en local por terminal
 - pip install -e .
 - pip install python-telegram-bot --upgrade

 Desde Visual Studio Code
 - https://pypi.org/project/python-telegram-bot/



Reto 4 - Snake

Juego de los 90 que todo móvil Nokia incorporaba de serie ^_^.
Un pequeño cubo se mueve por la pantalla en las siguientes direcciones :
    - UP
    - DOWN
    - LEFT
    - RIGHT
Éste debe de 'colisionar' con los elementos aleatorios (frutas) para ir creciendo.
Si la serpiente colisiona con la comida, incrementa el score en 1.
Si la serpiente colisiona con ella misma muere.
Fíjate en los límetes de la pantalla, si sales fuera, mueres.

Test Suite

def test_dead_in_top():
    snake = Snake()
    game = Game()

    snake.position = [512, 50]

    game.dead(snake)
    assert(game.run == False)

def test_dead_in_bot():
    snake = Snake()
    game = Game()

    snake.position = [0, 50]

    game.dead(snake)
    assert(game.run == False)

def test_dead_in_left():
    snake = Snake()
    game = Game()

    snake.position = [200, 512]

    game.dead(snake)
    assert(game.run == False)

def test_dead_in_right():
    snake = Snake()
    game = Game()

    snake.position = [200, 0]

    game.dead(snake)
    assert(game.run == False)

def test_live():
    snake = Snake()
    game = Game()

    snake.position = [100, 50]

    game.dead(snake)
    assert(game.run == True)

def test_score_plus():
    snake = Snake()
    game = Game()

    snake.position = game.food_pos

    game.eat(snake)
    assert(game.score == 1)

def test_food_random():
    game = Game()

    food1 = game.food_pos
    game.food_spawn()
    food2 = game.food_pos

    assert(food1 != food2)

def test_controller_snake_UP():
    snake = Snake()
    class event:
        type = 0
        key = 2
    
    class pygame:
        KEYDOWN = 0
        K_RIGHT = 0
        K_LEFT = 1
        K_UP = 2
        K_DOWN = 3

    snake.controller(event, pygame)

    assert(snake.change == "UP")

def test_controller_snake_DOWN():
    snake = Snake()
    class event:
        type = 0
        key = 3
    
    class pygame:
        KEYDOWN = 0
        K_RIGHT = 0
        K_LEFT = 1
        K_UP = 2
        K_DOWN = 3

    snake.controller(event, pygame)

    assert(snake.change == "DOWN")

def test_controller_snake_LEFT():
    snake = Snake()
    class event:
        type = 0
        key = 1
    
    class pygame:
        KEYDOWN = 0
        K_RIGHT = 0
        K_LEFT = 1
        K_UP = 2
        K_DOWN = 3

    snake.controller(event, pygame)

    assert(snake.change == "LEFT")

def test_controller_snake_RIGHT():
    snake = Snake()
    class event:
        type = 0
        key = 0
    
    class pygame:
        KEYDOWN = 0
        K_RIGHT = 0
        K_LEFT = 1
        K_UP = 2
        K_DOWN = 3

    snake.controller(event, pygame)

    assert(snake.change == "RIGHT")

def test_direction_snake_UP():
    snake = Snake()

    position_o = [100, 50]
    snake.change = "UP"
    snake.direction = "RIGHT"

    snake.changeDirection()

    assert(snake.direction == "UP")
    assert(snake.position[1] == (position_o[1] - 10))

    del snake

def test_direction_snake_DOWN():
    snake = Snake()

    position_o = [100, 40]
    snake.change = "DOWN"
    snake.direction = "RIGHT"

    snake.changeDirection()

    assert(snake.direction == "DOWN")
    assert(snake.position[1] == (position_o[1] + 10))

    del snake

def test_direction_snake_LEFT():
    snake = Snake()

    position_o = [100, 50]
    snake.change = "LEFT"
    snake.direction = "UP"

    snake.changeDirection()

    assert(snake.direction == "LEFT")
    assert(snake.position[0] == (position_o[0] - 10))

def test_direction_snake_RIGHT():
    snake = Snake()

    position_o = [90, 50]
    snake.change = "RIGHT"
    snake.direction = "UP"
    snake.changeDirection()

    assert(snake.direction == "RIGHT")
    assert(snake.position[0] == (position_o[0] + 10))


Dependencias en local por terminal
 - pip install -e .
 - git submodule update --init --recursive
 - pip install pygame

 Desde Visual Studio Code
 - https://pypi.org/project/pygame/



Empezamos GEEKS!!!!!!!!

```

## Referencias


* [Tutorial - Testing Automatizado](https://github.com/GeeksHubsAcademy/2020-js-vanilla-testing-FFFF/blob/master/README.md)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Telegram-Bot](https://pypi.org/project/python-telegram-bot/)
* [Pygame](https://pypi.org/project/pygame/)