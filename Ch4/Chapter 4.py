# 4.1 Using Functions

# Stored (and Reused) Steps

#def thing(): 
    #print ("Hello")
    #print("Fun")

#thing()
#print("Zip")
#thing()    
 
 # Max Function

#big = max("Hello world")
#print(big)

# Type Conversions

#print(float(99)/100)
#i = 42
#type(i)
#f = float(i)
#print(f)
#print(1 + 2 * float(3)/4-5)

# Parameters

def greet(lang):
    if lang == "es":
        print("Hola")
    elif lang == "fr":
        print("Bonjour")
    else:
        print("Hello")        
greet("es")
greet("en")

# Return values

def greet():
    return "Hello"

print(greet() , "Glenn")
print(greet() , "Sally")    

def greet(lang):
    if lang == "es":
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hello"        

print(greet("en") , "Glenn")
print(greet("es") , "Sally")  
print(greet("fr") , "Michael")  

# Arguments, Parameters, and Results
# Argument: "Hello world"
# Parameter: inp
# Result: w

big = max("Hello world")
print(big)

# Multiple Parameters / Arguments

# We can define more than one parameter in the function definition
# We simply add more arguments when we call the function
# We match the number and order of arguments and parameters

def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)    


def thing():
    print('Hello') 

print('There')

def func(x) :
    print(x)

func(10)
func(20)

def stuff():
    print('Hello')
    return
    print('World')

stuff()