# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 11:29:26 2018

@author: sripe
"""
import random
import time

def print_board(board_squares,square_id):
    edge = [['0' for i in range(board_squares[1])] for j in range(board_squares[0])] # Initiates list with zeroes

    for i in range(board_squares[0]):
        for j in range(board_squares[1]):
            if len(str(square_id[i][j])) < 2:
                edge[i][j] = ' | '
            elif len(str(square_id[i][j])) < 3:
                edge[i][j] = '| '



    print(' ___ '+(board_squares[1]-2)*'___ '+'___')
    for i in range(board_squares[0]-1):
    
        print('|'+board_squares[1]*'   |')
        print('| '+''.join([(str(square_id[i][j])+edge[i][j]) for j in range(board_squares[1])]))
        print('|'+board_squares[1]*'   |')
        print('|\u203E\u203E\u203E'*board_squares[1]+'|')
        
    print('|'+board_squares[1]*'   |')  
    print('| '+''.join([(str(square_id[board_squares[0]-1][i])+edge[board_squares[0]-1][i]) for i in range(board_squares[1])]))
    print('|'+board_squares[1]*'   |')    
    print(' '+'\u203E\u203E\u203E '*+board_squares[1])
    
    
to_win = 4
winner_kernel = [['X' for i in range(to_win)],['O' for i in range(to_win)]]
board_direction = ['horizontal', 'vertical']
board_dimensions = [4,8]
board_squares_input = [0,0] #Figure out how to define variable within loop
board_squares = [0,0] # Same goes for this!
i = 0 #Define in while loop?
winner = 0 #Winner is saved here





'''
Selecting Board dimension
'''
while i < len(board_direction): #Select the board dimensions. 
    board_squares_input[i] = input('Select the number of ' + board_direction[i] + ' squares[' + str(board_dimensions[0]) + '-' + str(board_dimensions[1]) + ']\n')
    board_squares[i] = int(board_squares_input[i])
    if (board_squares[i] < board_dimensions[0] or board_squares[i]>board_dimensions[1]):
        print('The number of squared is not valid, try again.')
        continue
    i = i+1
    
'''
Assignes a number to each square, based on the previous selection of squares
'''
k = 1 # Gives the inital number for the squares
square_id = [[0 for i in range(board_squares[1])] for j in range(board_squares[0])] # Initiates list with zeroes
square =  [[0 for i in range(board_squares[1])] for j in range(board_squares[0])] #square is where the X and Os are printed
occupied_dummies = [[0 for i in range(board_squares[1])] for j in range(board_squares[0])] #Dummie values to indicate if a square has already been taken.

for i in range(board_squares[0]): #Nested for loops, which assignes the numer from each square.
    for j in range(board_squares[1]):
        square_id[i][j] = k
        square[i][j] = k
        k = k+1

'''
Printing the board
'''

print('\n\n\nThis is the board you selected')
print_board(board_squares,square)

'''
Gives a name to the two players 
'''
player_1 = input('Player 1, what is your name?\n')
player_2 = input('Player 2, what is your name?\n')


rand = random.randint(0,1) #Assignes a random number, which decides who is goning to start.

'''
Welcomes the players, and prints the starter.
'''

print('Welcome ' + player_1 + ' and ' + player_2)
time.sleep(1)

if rand == 1:
    print(player_1,'is first!')
    first_player = player_1
    second_player = player_2
    
else:
    print(player_2,'is first!')
    first_player = player_2
    second_player = player_1    
time.sleep(0.5)

while True:
    
    taken_number_test = 0 #'Figures out' if an number is already taken
    i = 0
    j = 0
    
    print(first_player,'To move')
    
    while i < board_squares[0]:
        if taken_number_test == 0:
            user_input = input('Select a number ')
            user_input_to_int = int(user_input)
            taken_number_test = 1 
        while j < board_squares[1]:
            if taken_number_test == 0:
                break
            if user_input_to_int == square_id[i][j]:
                '''user_input_to_int == square_id[i][j] and '''
                if occupied_dummies[i][j] == 0:
                    square[i][j] = 'X'
                    occupied_dummies[i][j] = 1
                    break
                else:
                    print(user_input_to_int,'is already taken!')
                    taken_number_test = 0
                    j = 0
                    continue
            j = j+1
        if taken_number_test == 0:
            continue
        j = 0
        i = i+1     
        
        
    print_board(board_squares,square)
    
    
    print(second_player,'To move')
    i = 0
    j = 0
    taken_number_test = 0
    while i < board_squares[0]:
        if taken_number_test == 0:
            user_input = input('Select a number ')
            user_input_to_int = int(user_input)
            taken_number_test = 1 
        while j < board_squares[1]: 
            if taken_number_test == 0:
                break
            if user_input_to_int == square_id[i][j]:
                '''user_input_to_int == square_id[i][j] and '''
                if occupied_dummies[i][j] == 0:
                    square[i][j] = 'O'
                    occupied_dummies[i][j] = 1
                    print(str(square_id[i][j])+'is taken')
                    break
                else:
                    print(user_input_to_int,'is already taken!')
                    taken_number_test = 0
                    j = 0
                    i = 0
                    continue
                    #continue
            j = j+1
        if taken_number_test == 0:
            continue
        j = 0
        i = i+1 
    
    print_board(board_squares,square)
    
    '''
    Figure out who is winning
    '''
    hor = square
    ver = [[square[j][i] for j in range(len(square))] for i in range(len(square[0]))] 
    '''
    Winner in the vertical direction?
    '''
    for i in range(len(ver)): #Testing the vertical lines, to determine a winner
        if len(ver) > len(winner_kernel[0]):
            for j in range((len(ver))-len(winner_kernel[0])+1):
               # print(str(i)+','+str(j)+':'+str((j+len(winner_kernel[0]))))
                
                if ver[i][j:(j+len(winner_kernel[0]))] == winner_kernel[0]:
                    winner = first_player
                    print('first_player is winning')
                if ver[i][j:(j+len(winner_kernel[0]))] == winner_kernel[1]:
                    winner = second_player
                   
        else:
            for k in range(len(square[0])):
                if ver[k] == winner_kernel[0]:
                    winner = first_player
                   
                elif ver[k] == winner_kernel[1]:
                    winner = second_player
                   
    '''
    Winner in the horizontal diection?
    '''
    for i in range(len(hor)): #Testing the horizontal lines, to determine a winner
        if len(hor) > len(winner_kernel[0]):
            
            for j in range(len(hor)-len(winner_kernel[0])+1):
                if hor[i][j:(j+len(winner_kernel[0]))] == winner_kernel[0]:
                    winner = first_player
                    print('first_player is winning')
                   
                if hor[i][j:(j+len(winner_kernel[0]))] == winner_kernel[1]:
                    winner = second_player
                   
        else:
            for k in range(len(hor)):
                if hor[k] == winner_kernel[0]:
                    winner = first_player
                    
                elif hor[k] == winner_kernel[1]:
                    winner = second_player
                    
                
    if winner != 0:
        break
    
print_board(board_squares,square)
print('The winner is ' + winner)