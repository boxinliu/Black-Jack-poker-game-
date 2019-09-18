from IPython.display import clear_output
import random



def display_board(board):
    clear_output()
    print('|' + board[1]+'|'+board[2]+'|'+board[3]+'|')
    print('--------')
    print('|' + board[4]+'|'+board[5]+'|'+board[6]+'|')
    print('--------')
    print('|' + board[7]+'|'+board[8]+'|'+board[9]+'|')

test_board=[' ']*10

#display_board(test_board)
#display the board with 9 empty space 
    
# Set the game up here
def choose_first():
    rand=random.randint(1,2)
    if rand==1:
        return 'player1' 
    else:
        return 'player2'

def place_marker(board, marker, position):
    board[position]=marker


def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position=input('choose a position 1-9 ')
        return position

def space_check(board, position):
    if board[position] == ' ':
        return True 

    else:
        print('There is no space on board postion {} '.format(position))

def full_board_check(board):
    for i in range (1,10):

        if board[i] ==' ': #return true if it is full
            return False

    return True 

def win_check(board, mark):
    win_metrix = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[2,5,8],[3,5,7],[1,4,7],[3,6,9]]
    for a,b,c in win_metrix:
        if board[a]==board[b]==board[c]==mark:
            return True 
    return False

def replay():
    a = input('Do you want to play one more time? yes or no ')
    if a == 'yes':
        return True 


print('Welcome to Tic Tac Toe!')

while True:
    
    ask=input('Do you want to play the game? yes or no ')
    if ask =='yes' or ask=='y' or ask=='YES'or ask=='Y':
        Ask_func=True
        game_on=True
    elif ask =='no' or ask=='n'or ask=='NO'or ask=='N':
        game_on=False
        Ask_func=False
        break
    else: 
        game_on=False
        print('please type yes or no')

    while Ask_func:    
        display_board(test_board)
        ask2=input('Do you want to get X or O? ')
        if ask2 != 'X' and ask2!= 'O':
            print('You have to choose either X or O ')

        elif ask2 =='X':
            player1='X'
            player2='O'       
            print ('player1: ' + player1, '\n' + 'player2: ' + player2)
                    #put mark into board[postion] for player1 then go for the other mark for player2 
        elif ask2 =='O':
            player1='O'
            player2='X'
            print ('player1: ' + player1, '\n' + 'player2: ' + player2)     
        else: 
            print('you have to choose X or O ')

        choose_first()
        firstP = choose_first()
        print(firstP+ ' will start first! ')


        # play or not --> if play, choose X/O --> player1/2 will go first -->player1/2 mark goes into board[position] 

        while game_on:


            firstP =='player1'
            if full_board_check(test_board)==False:
                position_num = int(player_choice(test_board))        
                place_marker(test_board, player1, position_num)
                display_board(test_board)
            else:
                if win_check(test_board, player1):
                    print('game over! player1 won the game ')
                    game_on=False
                elif win_check(test_board, player2):
                    print('game over! player2 won the game ')
                    game_on=False
                elif full_board_check(test_board) and win_check(test_board, mark)==False: 
                    print('tie game! ')
                    game_on=False
                else:
                    firstP=='player2'


                    # Player2's turn.


            firstP =='player2' 
            if full_board_check(test_board)==False:
                position_num = int(player_choice(test_board))        
                place_marker(test_board, player2, position_num)
                display_board(test_board)
            else:
                if win_check(test_board, player1):
                    print('game over! player1 won the game ')
                    game_on=False
                elif win_check(test_board, player2):
                    print('game over! player2 won the game ')
                    game_on=False
                elif full_board_check(test_board) and win_check(test_board, mark)==False: 
                    print('tie game! ')
                    game_on=False
                else:
                    firstP=='player1'



        if not replay():
            break