import random
import os
from pytimedinput import timedInput
# from services.snake_service import *


class GameService:
    DIRECTIONS = {
        'w': (-1, 0),
        's': (1, 0),
        'd': (0, 1),
        'a': (0, -1)

    }

    @classmethod
    def generate_random_apple(cls, gameObj):
        apple_x = random.randint(1, gameObj.dimension[0] - 1)
        apple_y = random.randint(1, gameObj.dimension[1] - 1)
        while (apple_x, apple_y) in gameObj.snake.snake_coordinates:
            apple_x = random.randint(1, gameObj.dimension[0] - 1)
            apple_y = random.randint(1, gameObj.dimension[1] - 1)
        return apple_x, apple_y

    @classmethod
    def update_apple_pos(cls, gameObj):
        gameObj.apple = cls.generate_random_apple(gameObj)

    @classmethod
    def print_game(cls, gameObj):
        os.system('cls')
        for i in range(gameObj.dimension[0]):
            for j in range(gameObj.dimension[1]):
                if i == 0 or j == 0 or i == gameObj.dimension[0] - 1 or j == gameObj.dimension[1] - 1:
                    print('#', end=' ')
                elif (i, j) in gameObj.snake.snake_coordinates:
                    print('X', end=' ')
                elif (i, j) == gameObj.apple:
                    print('a', end=' ')
                else:
                    print(' ', end=' ')
            print()

    @classmethod
    def validate(cls, game_obj):
        return all([(0 < sc[0] < game_obj.dimension[0]-1 and 0 < sc[1] < game_obj.dimension[1]-1) for sc in game_obj.snake.snake_coordinates])

    @classmethod
    def update_snake_head(cls, game_obj, direction):

        snake_head = game_obj.snake.snake_coordinates[-1]
        new_snake_head = (cls.DIRECTIONS[direction][0] + snake_head[0], cls.DIRECTIONS[direction][1] + snake_head[1])
        # if new_snake_head is same as apple increase the length of the snake by 1 i.e just push new snake head
        if new_snake_head == game_obj.apple:
            game_obj.snake.snake_coordinates.append(new_snake_head)
            GameService.update_apple_pos(game_obj)
        # else pop tail and push new snake_head
        else:
            game_obj.snake.snake_coordinates.pop(0)
            game_obj.snake.snake_coordinates.append(new_snake_head)

    @classmethod
    def start_game(cls, game_obj):
        game_obj.apple = cls.generate_random_apple(game_obj)
        cls.print_game(game_obj)
        last_input = 'd'
        while 1:
            # i is input and 1s is timeout
            i, timed_out = timedInput("", 0.3)
            if i == 'q':
                print('Your score : {}'.format(game_obj.get_score()))
                break
            elif i != last_input and i in cls.DIRECTIONS.keys():
                # if get head of snake, and append updated snake head so that snake size increases by 1
                cls.update_snake_head(game_obj, i)
                last_input = i

                cls.print_game(game_obj)
            else:
                # if no input, move snake in last imput direction

                cls.update_snake_head(game_obj, last_input)
                cls.print_game(game_obj)
            snake_head = game_obj.snake.snake_coordinates[-1]
            if not cls.validate(game_obj):
                print('Your score : {}'.format(game_obj.get_score()))
                break

