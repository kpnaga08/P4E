from asyncore import loop
from inspect import getlineno
from operator import indexOf
from sqlite3 import SQLITE_ANALYZE
from stat import FILE_ATTRIBUTE_NO_SCRUB_DATA


Question 1
What is wrong with this Python loop:

n = 5
while n > 0 :
    print(n)
print('All done')

This loop will run forever
The print('All done') statement should be indented four spaces
There should be no colon on the while statement
while is not a Python reserved word

Answer: This loop will run forever

Question 2
What does the break statement do?

Exits the program
Resets the iteration variable to its initial value
Jumps to the "top" of the loop and starts the next iteration
Exits the currently executing loop

Answer: Exits the currently executing loop

Question 3
What does the continue statement do?

Exits the program
Exits the currently executing loop
Resets the iteration variable to its initial value
Jumps to the "top" of the loop and starts the next iteration

Answer: Jumps to the "top" of the loop and starts the next iteration

Question 4
What does the following Python program print out?

tot = 0 
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)

5
0
15
10

Answer: 5

Question 5
What is the iteration variable in the following Python code:

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
     print('Happy New Year:',  friend)
print('Done!')

friend
Glenn
Sally
friends

Answer: friend

Question 6
What is a good description of the following bit of Python code?

zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)

Compute the average of the elements in a list
Count all of the elements in a list
Find the smallest item in a list
Sum all the elements of a list

Answer: Sum all the elements of a list

Question 7
What will the following code print out?

smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)

Hint: This is a trick question and most would say this code has a bug - so read carefully

-1
74
42
3

Answer: -1

Question 8
What is a good statement to describe the is operator as used in the following if statement:

if smallest is None :
     smallest = value

The if statement is a syntax error
Looks up 'None' in the smallest variable if it is a string
matches both type and value
Is true if the smallest variable has a value of -1

Answer: matches both type and value

Question 9
Which reserved word indicates the start of an "indefinite" loop in Python?

indef
for
def
break
while

Answer: while

Question 10
How many times will the body of the following loop be executed?

n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')

This in an infinite loop
0
5
1

Answer: 0


