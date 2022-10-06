# Chapter 5: Loops and Iteration

# Repeated Steps

n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff!")
print(n)    

# Another Loop

n = 0
while n > 0:
    print("Lather")
    print("Rinse")
print("Dry off!")    

# Breaking out of a loop

while True:
    line = input(">")
    if line == "done":
        break
    print(line)
print("Done!")    

# Finishing an Iteration with Continue

The continue statement ends the current iteration and jumps to the top of the loop and starts the next iteration.

while True:
    line = input(">")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("Done!")  

# A simple Definite Loop

for i in [5, 4, 3, 2, 1]:
    print(i)
print("Blastoff!")    

# A Definite Loop with Strings

friends = ["Joseph", "Glenn", "Sally"]
for friend in friends:
    print("Happy New Year: ", friends)
print("Done!")

# Finding The Largest Value: Looping through a set

print("Before")
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print("After")    

# Another finding the largest value

Largest_so_far = 1
print("Before", Largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > Largest_so_far:
        Largest_so_far = the_num
    print(Largest_so_far, the_num)

print("After", Largest_so_far)        


# Counting in a Loop

zork = 0
print("Before", zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print("After", zork)   

# Summing in a loop

sum = 0
print("Before", sum)
for thing in [9, 41, 12, 3, 74, 15]:
    sum = sum + thing
    print(sum, thing)
print("After", sum)  

# Finding the Average in a Loop

count = 0
sum = 0
print("Before", count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("After", count, sum, sum/count)

# Filtering in a Loop: We use an if statement in the loop to catch/filter the values we are looking for.

print("Before")
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print ("Large number", value)
print("After")       

# Search using a Boolean Variable : if we just want to search and know if a value was found, we use a variable that starts at False and is set to True as soon as we find what we are looking for.

found = False
print("Before", found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print("After", found)        

# How to find the smallest value

Smallest_so_far = 100
print("Before", Smallest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num < Smallest_so_far:
        Smallest_so_far = the_num
    print(Smallest_so_far, the_num)

print("After", Smallest_so_far)  

# We still have a variable that is the smallest so far. The first time through the loop smallest is None, so we take the first value to be the smallest

Smallest = None
print("Before")
for value in [9, 41, 12, 3, 74, 15]:
    if Smallest is None:
        Smallest = value
    elif value < Smallest:
        Smallest = value    
    print(Smallest, value)

print("After", Smallest)  
