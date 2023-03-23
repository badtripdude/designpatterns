from abc import ABC, abstractmethod


class Game(ABC):
    def __init__(self, num_of_players):
        self.num_of_players = num_of_players
        self.cur_player = 0

    def run(self):
        """This is template method"""
        self.start()
        while not self.have_winner:
            self.take_turn()
        print(f'Player {self.winning_player} wins!')

    @abstractmethod
    def start(self):
        ...

    @abstractmethod
    def take_turn(self):
        ...

    @property
    @abstractmethod
    def have_winner(self):
        ...

    @property
    @abstractmethod
    def winning_player(self):
        ...


class Chess(Game):
    def __init__(self):
        super().__init__(2)
        self.max_turn = 10
        self.turn = 1

    def take_turn(self):
        print(f'Turn {self.turn} taken by player '
              f'{self.cur_player}')
        self.turn += 1
        self.cur_player = 1 - self.cur_player

    def start(self):
        print(f'Starting a game of chess with '
              f'{self.num_of_players}')

    @property
    def have_winner(self):
        return self.turn >= self.max_turn

    @property
    def winning_player(self):
        return self.cur_player


if __name__ == '__main__':
    game = Chess()
    game.run()
