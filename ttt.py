# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 14:25:57 2018

@author: sripe
"""
import random
import time

square = [1,2,3,4,5,6,7,8,9]
occupied_dummies = [0,0,0,0,0,0,0,0,0] #To be used in the while loop to determine if a square is taken
taken_number_test = 0
i = 0




player_1 = input('Player 1, what is your name?\n')
player_2 = input('Player 2, what is your name?')

rand = random.randint(0,1)

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
time.sleep(1.5)

while True:
    
    print(' ___ ___ ___')
    print('|   |   |   |')
    print('|',square[0],'|',square[1],'|',square[2],'|')
    print('|   |   |   |')
    print('|\u203E\u203E\u203E|\u203E\u203E\u203E|\u203E\u203E\u203E|')
    print('|',square[3],'|',square[4],'|',square[5],'|')
    print('|   |   |   |')
    print('|\u203E\u203E\u203E|\u203E\u203E\u203E|\u203E\u203E\u203E|')
    print('|',square[6],'|',square[7],'|',square[8],'|')
    print('|   |   |   |')
    print(' \u203E\u203E\u203E \u203E\u203E\u203E \u203E\u203E\u203E ')
 
    #first player
    
    print(first_player,'To move')
    #user_input = input('Select a number ')
    #user_input_to_int = int(user_input)
    while i <= len(occupied_dummies):
        
        if taken_number_test == 0:
            user_input = input('Select a number ')
            user_input_to_int = int(user_input)
            taken_number_test = 1
            
        if user_input_to_int == i+1:
                
            if user_input_to_int == i+1 and occupied_dummies[i] == 0:
                square[i] = 'X'
                occupied_dummies[i] = 1
            else:
                print(user_input_to_int,'is already taken!')
                taken_number_test = 0
                i = 0
                continue

        i = i+1
    
    taken_number_test = 0
    i = 0
    
    print(' ___ ___ ___')
    print('|   |   |   |')
    print('|',square[0],'|',square[1],'|',square[2],'|')
    print('|   |   |   |')
    print('|\u203E\u203E\u203E|\u203E\u203E\u203E|\u203E\u203E\u203E|')
    print('|',square[3],'|',square[4],'|',square[5],'|')
    print('|   |   |   |')
    print('|\u203E\u203E\u203E|\u203E\u203E\u203E|\u203E\u203E\u203E|')
    print('|',square[6],'|',square[7],'|',square[8],'|')
    print('|   |   |   |')
    print(' \u203E\u203E\u203E \u203E\u203E\u203E \u203E\u203E\u203E ')

    
    
#Second player

    print(second_player,'To move')

    while i <= len(occupied_dummies):
        if taken_number_test == 0:
            user_input = input('Select a number ')
            user_input_to_int = int(user_input)
            taken_number_test = 1
            
        if user_input_to_int == i+1:
            
            if user_input_to_int == i+1 and occupied_dummies[i] == 0:
                square[i] = 'O'
                occupied_dummies[i] = 1
            else:
                print(i+1,'is already taken, try again')
                taken_number_test = 0
                i = 0
                continue
                
        i = i+1            
    taken_number_test = 0    
    i = 0           
                
    print(' ___ ___ ___')
    print('|   |   |   |')
    print('|',square[0],'|',square[1],'|',square[2],'|')
    print('|   |   |   |')
    print('|\u203E\u203E\u203E|\u203E\u203E\u203E|\u203E\u203E\u203E|')
    print('|',square[3],'|',square[4],'|',square[5],'|')
    print('|   |   |   |')
    print('|\u203E\u203E\u203E|\u203E\u203E\u203E|\u203E\u203E\u203E|')
    print('|',square[6],'|',square[7],'|',square[8],'|')
    print('|   |   |   |')
    print(' \u203E\u203E\u203E \u203E\u203E\u203E \u203E\u203E\u203E ')

    