

class Game:

    def __init__(self, snake, dimension=(16, 32), apple=None):
        self.dimension = dimension
        self.snake = snake
        self.coordinates = [[(i, j) for i in range(dimension[0])] for j in range(dimension[1])]
        self.apple = apple

    def get_score(self):
        return (len(self.snake.snake_coordinates) - self.snake.initial_snake_size)
