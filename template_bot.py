import chess
import random

from abc import ABC, abstractmethod


class ChessBotClass(ABC):
    @abstractmethod
    def __call__(self, board_fen: str) -> chess.Move:
        pass


# keep the bot named ChessBot when submitting
class ChessBot(ChessBotClass):
    def __call__(self, board_fen):
        board = chess.Board(board_fen)

        moves = list(board.legal_moves)

        idx = int(random.random() * len(moves))

        move = moves[idx]

        return move
