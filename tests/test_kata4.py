import pytest

from kata4.snake import Game, Snake

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
