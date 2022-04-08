def create_game():
    gameList = ['-','-', '-',
                '-', '-', '-',
                '-', '-', '-']
    return gameList

def select_starting_player(starter):
    if (starter == 'O'):
        return True
    else:
        return False

def output_game(values):
    index = 0
    for row in values:
        for column in row:
            index += 1
            print(column, end=" ")
            if (index % 3 == 0):
                print()


# Check winner
def check_horizontal_win(values):
    if values[0] == values[1]==values[2] and values[0] != '-':
        if values[0]=='X':
            return 'X'
        else:
            return 'O'
    if values[3] == values[4]==values[5] and values[3] != '-':
        if values[3]=='X':
            return 'X'
        else:
            return 'O'
    if values[6] == values[7]==values[8] and values[6] != '-':
        if values[6]=='X':
            return 'X'
        else:
            return 'O'

def check_vertical_win(values):
 if values[0] == values[3] == values[6] and values[0] != '-':
     if values[0] == 'X':
         return 'X'
     else:
         return 'O'
 if values[1] == values[4] == values[7]and values[1] != '-':
     if values[1] == 'X':
         return 'X'
     else:
         return 'O'
 if values[2] == values[5] == values[8]and values[2] != '-':
     if values[2] == 'X':
         return 'X'
     else:
         return 'O'

def check_diagonal_win(values):
 if values[0] == values[4] == values[8]and values[0] != '-':
     if values[0] == 'X':
         return 'X'
     else:
         return 'O'
 if values[2] == values[4] == values[6]and values[2] != '-':
     if values[2] == 'X':
         return 'X'
     else:
         return 'O'

def check_tie(index):
    if index == 9:
        return True