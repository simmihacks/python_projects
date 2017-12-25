#this is not code but a Pseudocode for an MIT coding challenge: 
#https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2017_2/courseware/530b7f9a82784d0cb57de334828e3050/bfe9eb02884a4812883ff9e543887968/?child=first
"""
Hangman Pseudo Code

1.	Load the words 
2.	Randomly Select a word
3.	Save the word in a string: secretword
4.	Ask the user to guess a letter from the 26 letters
5.	Save the letter in string: guess

6.	def check: See if the letter in variable guess is in secretword, return boolean

7.	def show: If the guess letter is present in secretword, only show the letters in the string that has been guessed right. This should return all the letters with _ (for the one not yet guessed) and the guessed letters.

8.	def available: Take out the correctly guessed letter from the alphabet, and show the ones remaining

9.	Make a counter that only lasts up to 8 guesses, and do the following:

a)	Start a for-loop for the counter of 8 guesses
b)	Ask the user to guess a letter by calling the 3rd def available function
c)	Check secretword; call def check
d)	If you guessed the letter twice, print: Oops! You've already guessed that letter
e)	If the letter not in secretword, print: Oops! That letter is not in my word
f)	If it is correct, print: Good guess
g)	All of the above, call def show so that the use can see what s/he has gotten right
"""
#Hope this helps 
