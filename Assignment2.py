#Assignment 2 

#importing the libraries needed for the code.
import random
import statistics

#We need to find the distance between two points 

#init for the distance variable 
distance = 0

#Init of the distance function that takes 3 parameters 
def distfunc(e, w, c):
    #Use try so we can catch a specific error
    try:
        #Declaring distance as a global variable
        global distance
        #if the length of the two points are not the same then print an error and exit the function
        if len(e) != len(w):
            #print that the dims aren't the same
            print('Not in the same dimension, unable to compute')
            #return the function 
            return
        #if c, the counter that was originally the length of the point, is greater than zero then do the following
        elif c > 0: 
            #Calculate the difference between x1 and x2 then square it
            distance = distance + ((e[c] - w[c]) ** 2)
        #if c is equal to zero, this being the last item in the point then do the following
        elif c == 0:
            #calculate the difference between, presumibly,y1 and y2
            distance = distance + ((e[c] - w[c]) ** 2)
            #find the square root of the distance 
            distance = distance ** 0.5
            #print the distance
            print(distance)
            #return/end the function
            return
        #if none of the previous conditions are met then just return/end the function
        else:
            return
        #call the function again but take 1 away from the counter
        distfunc(e, w, (c-1))
    #if there is an error and it is a index error then print the following
    except IndexError: 
        print('You entered the dimension too high. We start at 0 here!')
#define the points and the length of the first list as the counter
ds1 = [2,4]
ds2 = [7,6]
leg = len(ds1) - 1
#call the function with the points and the counter
distfunc(ds1,ds2,leg)

#to use the for loop we need to declare the distance variable
distance1 = 0
#for the length of the first point then calculate the distance of the points
for i in range(len(ds1)):
    #find the diff and square it.
    distance1 += (ds1[i] - ds2[i]) ** 2 
#get the sqrt of the distance
distance1 = distance1 ** 0.5
#print the distance
print(distance1)

#for the coin flips, 0 = tails and 1 = heads
#init the outcomes list
outcome = []
#setting the seed for random so we get the same results everytime. This is just for the assignment and would be like this in a real solution
random.seed(42)
#init the mode variable
mo = 0
#make the function for coin flips. It will take 1 param
def coinflips(times):
    #if the times is equal to zero the calculate the mode
    if times == 0:
        #try to do calc the mode and print mode of the list
        try:
            mo = statistics.mode(outcome)
            print("The mode was: " + str(mo))
            return outcome
        except statistics.StatisticsError:
            #if there was a stat error then print that they both occured equally as that's the only cause of the error.
            print("Both occured equally. Try again.")
            return 
    #if the times is not equal to zero then generate a random number that is eiter 0 or 1
    else: 
        outcome.append(random.randint(0,1))
    #call the coinflip function and take 1 away
    coinflips(times-1)
#define the flips variable for the function
flips = 3
coinflips(flips)

#define the list for the for loop to hold the flips
loopout = []
#loop through flips and generate 0 or 1
for i in range(flips):
    loopout.append(random.randint(0,1))
#try to find mode and print the mode
try: 
    mo1 = statistics.mode(loopout)
    print('The mode for the iteration was: ' + str(mo1))
#if there was an equal amount of 0 and 1 then print they were both equal
except statistics.StatisticsError:
    print("Both occurred equally. Try again.")
    
