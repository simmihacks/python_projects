# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 2017
@author: simmihacks
the user thinks of a numbers and the computer tries to guess that number using bisection search
"""

#Secret Number Game; guess my number
low=0
high=100
print("Please think of a number between 0 and 100!")
secretnum=(low+high)//2
while True:
      print("Is your secret number "+str(secretnum)+ "?")
      s = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly! ")
      if len(s) > 1:
         print("Sorry, I do not understand your input.")
      elif s[0] != 'h' and s[0] != 'l' and s[0] != 'c':
         print("Sorry, I did not understand your input.")
      elif s[0] == 'h':
          high=secretnum
          secretnum=(low+secretnum)//2
      elif s[0] =='l':
          low=secretnum
          secretnum=(high+secretnum)//2
          
      elif s[0] == 'c':
         print("Game over. Your secret number was: " +str(secretnum))
         
         print("Do you want to play again?")
         p = input("Enter 'y' to play. Enter 'n' to quit the game.")
         if len(p) > 1:
             print("Sorry, please enter either y or n.")
         elif p[0] != 'y' and p[0] != 'n':
             print("Sorry, enter either y or n. ")
         elif p[0]== 'n':
             print('Thanks for Playing my first game')
             break
