# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 10:25:25 2019

@author: brand
"""
#Assignment 1
# 1.1

import datetime as dt  #importing datetime to get the current date of the user 
import pandas as pd #importing pandas to get quarter and dayofweek functions
today = dt.datetime.today() #getting the current date of the user
pToday = pd.Timestamp(today) #Converting the date to a pandas timestamp so it can be used with other pandas functions.
#
if (pToday.quarter > 2): #First layer of the conditional to check if the quarter is after Q2.
    if(pToday.dayofweek  > 0 and pToday.dayofweek < 4): #Checking if the day of the week is between 0 and 4
        print("It is time to put out the Christmas products!") #if both then print that it's time to put out the christmas products
    else:
        print("It is time to put the Christmas products but you need to wait until Monday.") #if it's after the 2nd quarter but it's later in the week then this will print. 
else:
    print("It's not even June yet! It is not time to put out the Christmas products.") #if it's q1 or q2 then this will print. 
    
# 1.2

make = input("What brand is the vehicle?") #Getting the input from the user for the make of the vehicle
modelType = input("What type of vehicle is it?") #Getting the input for the model type of the vehicle
make = make.lower() #making the make lowercase in case the user adds upper case and make it easier to write conditionals on the input
modelType = modelType.lower() #Again, making lowercase to make it easier for us to use conditionals. 
if(make == "ford" or make == "chevy" or make == "gmc"): #if the make is anything that is considered 'american' made it'll pass as true and go to the next conditional. 
    if(modelType == "truck"): #if the model type is a truck then travis will buy it. 
        print("Tarvis bought it!") #print statement of travis buying the vehicle is printed
    else: #if it's not a truck then travis doesn't want it.
        print("Tarvis doesn't want that!")
else: #if it's not american then travis doesn't want it either.
    print("Tarvis doesn't want that!")
    
#2.1 
    
menu = {0:['Grilled Salmon'],1:['Baked Chicken'],2:['Shrimp Pasta']} #declaring the menu dictionary 
for i in menu: #init for the for loop
    menu[i].append('Salad') #appending salads to each item in the dictionary
print(menu.items()) #printing each item of the dictionary to see if the salad was added. 
#2.2

import random #import random for the use of random ints
i = 1 #init i as 1 for the while loop. 
while(i < 11): #init the while loop
    r1 = random.randint(1,20) #init r1 as a random int between 1 and 20
    r2 = random.randint(1,25) #init r2 as a random int between 1 and 25
    r3 = r1 * r2  #multipling the two variables
    print("Molly's number is ",r3) #print the numbers after computing 
    i+=1 #increment the counter.

