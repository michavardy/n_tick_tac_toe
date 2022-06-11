import string

class TTT():
    def __init__(self, players: int, n: int):
        self.num_players = players
        self.n = n
        self.moves_made = 0
        self.symbols = ['X', 'O', '@', '$', '&', '*', '!', '~', 'H', 'C', 'D']
        self.player = 1
        self.board = [[False for i in range(self.n)] for i in range(self.n)]
    
    def disp(self):
        print(', '.join([f'player {i+1}: {self.symbols[i]}' for i in range(self.num_players)]))
        print('   ' + '  '.join([string.ascii_uppercase[i] for i in range(len(self.board))]))
        print("  " + '-'*(len(self.board)*3 + 1))
        for row_index, row in enumerate(self.board):
            print(f'{row_index + 1} |', end = ' ')
            for val in row:
                if not val:
                    print(' |', end = ' ')
                else:
                    print(f'{val}|', end = ' ')
            print('')
            print("  " + '-'*(len(self.board)*3 + 1))

    def move_input(self):
        print(f'player: {self.player}')
        return(input('select cell: '))
    
    def update_move(self, val: str ):
        col = string.ascii_uppercase.index(val[0])
        row = int(val[1]) - 1
        if self.board[row][col]:
            print('this cell is already taken')
        else:
            self.board[row][col] = self.symbols[self.player - 1]
    
    def next_player(self):
        if self.player == self.num_players:
            self.player = 1
        else:
            self.player = self.player+1
    
    def move(self):
        val = self.move_input()
        self.update_move(val)
        self.next_player()
        self.moves_made = self.moves_made + 1
    
    def check_horizontal(self):
        if any([len(set(row)) == 1 for row in self.board if any(row)]):
            return(True)
        else:
            return(False)
    
    def check_vertical(self):
        columns =  [[row[col_index] for row in self.board] for col_index in range(len(self.board))]
        if any([len(set(col)) == 1 for col in columns if any(col)]):
            return(True)
        else:
            return(False)

    def check_diagnal(self):
        diag1 = [self.board[i][i]  for i in range(len(self.board))]
        diag2 = [self.board[self.n-i][i-1]  for i in range(len(self.board),0,-1)]
        diag = [diag1, diag2]
        if any([len(set(d)) == 1 for d in diag if any (d)]):
            return(True)
        else:
            return(False)

    def checkWin(self):
        if self.check_horizontal() or self.check_vertical() or self.check_diagnal():
            return(True)
        else:
            return(False)

def main():
    players = input('how many players: ')
    n = input('grid dimensions nxn: ')
    ttt = TTT(int(players), int(n))
    while not ttt.checkWin():
        ttt.disp()
        ttt.move()

    print('good game')
    return(ttt)


if __name__ == '__main__':
    ttt = main()