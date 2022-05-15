class Board:
    BOARD_MAPPING = {0: "North-West", 1: "North", 2: "North-East",
                     3: "West", 4: "Centre", 5: "East",
                     6: "South-West", 7: "South", 8: "South-East"}
    WIN_CONDITIONS = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    board = [""] * 9

    def p1_win(self):
        x_squares = []
        for square in self.board:
            x_squares.append(square == "x")
        for condition in self.WIN_CONDITIONS:
            if x_squares[condition[0]] and x_squares[condition[1]] and x_squares[condition[2]]:
                return True
        return False

    def p2_win(self):
        o_squares = []
        for square in self.board:
            o_squares.append(square == "o")
        for condition in self.WIN_CONDITIONS:
            if o_squares[condition[0]] and o_squares[condition[1]] and o_squares[condition[2]]:
                return True
        return False

    def full_board(self):
        return self.board.count("") == 0

    def board_state(self):
        output = ""
        for index, item in enumerate(self.board):
            # print(index, item)
            if item == "":
                output = output + " "
            else:
                output = output + item
            # print(index + 1 % 3)
            if (index + 1) % 3 != 0:
                output = output + "|"
            elif index + 1 % 3 != 0 and index != 8:
                output = output + "\n-----\n"
        return output

    def p1_move(self):
        message = "Player 1, please select square to place marker: "
        for index, square in enumerate(self.board):
            if square == "":
                message = message + self.BOARD_MAPPING[index] + f"({index + 1}), "
        square_value = input(message)
        self.board[int(square_value) - 1] = "x"

    def p2_move(self):
        message = "Player 2, please select square to place marker: "
        for index, square in enumerate(self.board):
            if square == "":
                message = message + self.BOARD_MAPPING[index] + f"({index + 1}), "
        square_value = input(message)
        self.board[int(square_value) - 1] = "o"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = Board()
    while not board.p1_win() and not board.p2_win() and not board.full_board():
        board.p1_move()
        print(board.board_state())
        if board.p1_win():
            print("Player 1 wins")
            break
        board.p2_move()
        print(board.board_state())
    if board.p2_win():
        print("Player 2 wins")
    elif board.full_board():
        print("Tie game")
