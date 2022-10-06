# Chapter Three: Conditional Code

# In this section we move from sequential code that simply runs one line of code after another to conditional code where some steps are skipped. It is a very simple concept - but it is how computer software makes "choices".

# Boolean expressions: True / False or Yes / No

#x = int(input("x: ")) # 5
#if x == 5:
    #print('Equals 5')
#if x > 4:
    #print('Greater than 4')
#if x >= 5:
    #print('Greater than or Equals 5')
#if x < 6:
    #print('Less than 6')
#if x <= 5:
    #print('Less than or Equals 5')    
#if x != 6:
    #print('Not equal 6')            

 # One-way Decisions

#x = int(input("x: "))
#if x == 5: 
    #print('Is 5')
    #print('Is still 5')
    #print('Third 5')

#if x == 6: 
    #print('Is 6') #Afterwards 6
    #print('Is still 6')
    #print('Third 6')      
    #print('Afterwards 6')


# Nested Decisions

#x = int(input("x: "))
#if x > 1:
    #print('More than one')
    #if x < 100:
        #print('Less than 100')
#print('All done')            


 # Two-way Decisions

#x = int(input("x: "))
#if x > 2:
   #print('Bigger')
#else:
   #print('Smaller')
   #print('All done')        

# 3.2 More Conditional Statements

# elif is a combination between else and if 

# Multi-way

#x = int(input("x: "))
#if x < 2:
    #print('Small')
#elif x < 10:
    #print('Medium')
#elif x < 20:
   #print('Big')   
#elif x < 40:
    #print('Large')  
#elif x < 100:
    #print('Huge')     
#else:             
    #print('Ginormous')     


astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1   