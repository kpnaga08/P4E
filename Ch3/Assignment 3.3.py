# Assignment 3.3

# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.


Score = input('Enter score: ')

Sc= float(Score)

if Sc > 1:
    print("Error! Score exceeds 1.0")
if Sc >= 0.9 and Sc < 1:
    print ("A")
elif Sc >= 0.8 and Sc < 0.9:
    print ("B")    
elif Sc> 0.7 and Sc < 0.8:
    print ("C")    
elif Sc >= 0.6 and Sc < 0.7:
    print ("D")       
elif Sc < 0.6:
    print ("F")
 

