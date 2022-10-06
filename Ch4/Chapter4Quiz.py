from re import X
import threading


Question 1
Which Python keyword indicates the start of a function definition?

return
rad
continue
def


Answer: def

Question 2
In Python, how do you indicate the end of the block of code that makes up the function?

You put the colon character (:) in the first column of a line
You de-indent a line of code to the same indent level as the def keyword
You add a line that has at least 10 dashes
You put the "END" keyword in column 7 of the line which is to be the last line of the function

Answer: You de-indent a line of code to the same indent level as the def keyword

Question 3
In Python what is the input() feature best described as?

A built-in function
The central processing unit
A conditional statement
A user-defined function

Answer: A built-in function

Question 4
What does the following code print out?

def thing():
    print('Hello') 

print('There')

def
thing

There

thing

thing 
Hello 
There

Answer: There


Question 5
In the following Python code, which of the following is an "argument" to a function?

x = 'banana'
y = max(x)
z = y * 2

x
max
'banana'
y

Answer: x

Question 6
What will the following Python code print out?

def func(x) :
    print(x)

func(10)
func(20)

x
20

x 
10
x
20

def
x
func
func

10
20

Answer: 10
        20


Question 7
Which line of the following Python program will never execute?

def stuff():
    print('Hello')
    return
    print('World')

stuff()


print{"World"}
print("Hello")
def stuff()
return
stuff()

Answer: print("Hello")

Question 8
What will the following Python program print out?


def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('fr'),'Michael')


Bonjour Michael
Hola Michael
Hello Michael
def

Answer: Bonjour Michael


Question 9
What does the following Python code print out? (Note that this is a bit of a trick question and the code has what many would consider to be a flaw/bug - so read carefully).

def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)

14
7
addtwo
2

Answer: 2

Question 10
What is the most important benefit of writing your own functions?


To avoid having more than 10 lines of sequential code without an indent or de-indent
Avoiding writing the same non-trivial code more than once in your program
Following the rule that no function can have more than 10 statements in it
Following the rule that whenever a program is more than 10 lines you must use a function

Answer: 
Avoiding writing the same non-trivial code more than once in your program