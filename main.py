

from models.game import Game

from models.snake import Snake
from services.game_service import GameService


def run():
    snake = Snake([(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)])
    game = Game(snake)
    GameService.start_game(game)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
