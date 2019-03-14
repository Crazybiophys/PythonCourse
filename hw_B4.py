# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 23:32:47 2019

@author: Мой компьютер
"""

import time            
import random
start = time.time()
game = input('I want to play one game with you... Press ENTER to continue...')
if time.time() - start >= 5:
    print('You did not have time to jump into the train and died... Try again...')
else:            
    if game=='':
        print('I will think of number from 1 to 100. Your task is to guess the number. Lets go!')
        num=int(random.uniform(1,101))
        user=input('Enter integer from 1 to 100 you are thinking of: ')
        
       
        if user.isdigit()==True:
            user=int(user)
            while user!=num:
                '''if int(user)==0 and int(user)>101:
                    print('You broke the rules of the game...')
                    break'''
                if user>num and int(user)<101 and int(user)!=0:
                    user=input('Too large number... Enter other: ')
                    if user.isdigit()==False:
                        print('You broke the rules of the game...')
                        break
                    elif user.isdigit()==True and int(user)<101 and int(user)!=0:
                        user=int(user)
                        continue
                    else:
                        print('You broke the rules of the game...')
                        break
                    
                elif user<num and int(user)<101 and int(user)!=0:
                    user=input('Too small number... Enter other: ')
                    if user.isdigit()==False:
                        print('You broke the rules of the game...')
                        break
                    elif user.isdigit()==True and int(user)<101 and int(user)!=0:
                        user=int(user)
                        continue
                    else:
                        print('You broke the rules of the game...')
                        break
                else:
                    print('You broke the rules of the game...')
                    break
        else:
            print('You broke the rules of the game...')
                    
    if user==num:
        print('You won! Take a pie from the shelf!')
    else:
        print('You lose!')