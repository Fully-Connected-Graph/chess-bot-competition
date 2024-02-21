import chess
import random

from abc import ABC, abstractmethod


INF = 1e10


class ChessBotClass(ABC):
    @abstractmethod
    def __call__(self, board_fen: str) -> chess.Move:
        pass


# keep the bot named ChessBot when submitting
class ChessBot(ChessBotClass):
    def __init__(self, max_depth: int = 2) -> None:
        self._max_depth = max_depth

    def evaluate_board(self, board: chess.Board, color: chess.Color) -> float:
        return (
            sum([piece.color == color for piece in board.piece_map().values()])
            + random.random() * 0.1
            - 0.05
        )

    def minimax(
        self,
        depth: int,
        board: chess.Board,
        alpha: float,
        beta: float,
        maximizing: bool,
    ) -> float:

        if depth == 0 or board.is_game_over():
            return self.evaluate_board(board, board.turn) * -(1 ** (not maximizing))
        if maximizing:
            value = -INF
            for move in board.legal_moves:
                board.push(move)  # also switches turn
                value = max(
                    value, self.minimax(depth - 1, board, alpha, beta, not maximizing)
                )
                board.pop()
                if value > beta:
                    break
                alpha = max(alpha, value)
        else:
            value = INF
            for move in board.legal_moves:
                board.push(move)
                value = min(
                    value, self.minimax(depth - 1, board, alpha, beta, not maximizing)
                )
                board.pop()
                if value < alpha:
                    break
                beta = min(beta, value)
        return value

    def __call__(self, board_fen: str) -> chess.Move:
        board = chess.Board(board_fen)

        best_move = None
        best_eval = -INF
        for move in board.legal_moves:
            board.push(move)
            value = self.minimax(self._max_depth, board, -INF, INF, True)
            if value > best_eval:
                best_eval = value
                best_move = move
            board.pop()
        return best_move
