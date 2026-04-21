human = 'O'
computer = 'X'

board_screen = ' 0 | 1 | 2\n 3 | 4 | 5\n 6 | 7 | 8\n'

board = [" "] * 9

win_status = [(0,1,2),(3,4,5),(6,7,8),
              (0,3,6),(1,4,7),(2,5,8),
              (0,4,8),(2,4,6)]

print('========Tic-Tac-Toe=======')

def show_board():
    print(board_screen)
    pass

def is_win(turn):
    for status in win_status:
        if board[status[0]] == board[status[1]] == board[status[2]] == turn:
            return True
    return False

def computer_num():
    for i in range(len(board)):
        if board[i] == " ":
            return i
    return -1

def update_game(number,who):
    global board_screen
    global board
    board[number] = who
    board_screen = board_screen.replace(str(number),who)

show_board()

while True:
    human_input = int(input('숫자를 입력하세요'))
    update_game(human_input,human)
    show_board()
    if is_win(human): 
        print('You win ~~~~~~~~~!')
        break
    print('컴퓨터 차례입니다')
    computer_input = computer_num()
    if computer_input == -1:
        show_board()
        print("The game ended in a tie ~~~~~~~~~!")
        break
    update_game(computer_input,computer)
    show_board()
    if is_win(computer): 
        print('You loose ~~~~~~~~~!')
        break
    