import tic_tac_toe as game

gameList = game.create_game()
game.output_game(gameList)
playerX = input("Enter player X name")
playerO = input("Enter player O name")

index = 0
isTaken = False
winner = None


def takePosition(position):
    try:
        for value in range(len(gameList) + 1):
            if value == int(position):
                if gameList[value - 1] == '-':
                    gameList[value - 1] = starter
                    return True
                else:
                    print("SPOT TAKEN")
                    return False
    except ValueError:
        print("INVALID SPOT, must be numeric")


while winner is None:
    isTaken = False
    game.output_game(gameList)
    if index % 2 == 0:
        starter = 'X'
    else:
        starter = 'O'

    if starter == 'X':
        position = input(playerX.upper() + ": Choose your spot")
        isTaken = takePosition(position)
    else:
        position = input(playerO.upper() + ": Choose your spot")
        isTaken = takePosition(position)

    if isTaken:
        index += 1

    if game.check_tie(index):
        winner = "tie"
    if game.check_horizontal_win(gameList) is not None:
        winner = game.check_horizontal_win(gameList)
    elif game.check_vertical_win(gameList) is not None:
        winner = game.check_vertical_win(gameList)
    elif game.check_diagonal_win(gameList) is not None:
        winner = game.check_diagonal_win(gameList)

print("----------------------")
game.output_game(gameList)
if winner == 'X':
    print(playerX.upper() + " is the winner!")
elif winner == 'O':
    print(playerO.upper() + " is the winner!")
elif winner == "tie":
    print("There is no winner")
