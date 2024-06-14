import PySimpleGUI as sg


class TicTacToeUI:
    def __init__(self):
        self.current_player = 'X'
        layout = [
            [sg.Text('X Starts First')],
            [[sg.Button(size=(3, 1), key=(row, col)) for col in range(3)] for row in range(3)],
            [sg.Button('Reset'), sg.Button('Cancel')]
        ]
        self.window = sg.Window('Tic Tac Toe', layout)

    def run(self):
        while True:
            event, values = self.window.read()
            match event:
                case sg.WINDOW_CLOSED | 'Cancel':
                    break
                case 'Reset':
                    self.reset_game()
                case _:
                    self.window[event].update(self.current_player)
                    result = self.check(event)
                    if result:
                        choice = sg.popup_ok_cancel(f'{result}. Again?')
                        if choice == 'OK':
                            self.reset_game()
                            continue
                        else:
                            break
                    self.change_player()
        self.window.close()

    def reset_game(self):
        self.current_player = 'X'
        [self.window[(row, col)].update('') for col in range(3) for row in range(3)]

    def change_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check(self, event):

        if all(self.window[(event[0], row)].get_text() == self.current_player for row in range(3)):
            return f'{self.current_player} wins!'

        if all(self.window[(col, event[1])].get_text() == self.current_player for col in range(3)):
            return f'{self.current_player} wins!'
        if event[0] == event[1]:
            if all(self.window[(i, i)].get_text() == self.current_player for i in range(3)):
                return f'{self.current_player} wins!'
        if event in ((0, 2), (1, 1), (2, 0)):
            if all(self.window[(i, 2 - i)].get_text() == self.current_player for i in range(3)):
                return f'{self.current_player} wins!'

        return None


if __name__ == '__main__':
    game = TicTacToeUI()
    game.run()
