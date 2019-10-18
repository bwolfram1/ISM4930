#Assignment 2 
import random
import statistics


distance = 0
def distfunc(e, w, c):
    try:
        global distance
        if len(e) != len(w):
            print('Not in the same dimension, unable to compute')
            return
        elif c > 0: 
            distance = distance + ((e[c] - w[c]) ** 2)
        elif c == 0:
            distance = distance + ((e[c] - w[c]) ** 2)
            distance = distance ** 0.5
            print(distance)
            return
        else:
            return
        distfunc(e, w, (c-1))
    except IndexError: 
        print('You entered the dimension too high. We start at 0 here!')
ds1 = [2,4]
ds2 = [7,6]
distfunc(ds1,ds2,1)

distance1 = 0
for i in range(len(ds1)):
    distance1 += (ds1[i] - ds2[i]) ** 2
distance1 = distance1 ** 0.5
print(distance1)





outcome = []
mo = 0
def coinflips(times):
    global avg
    if times == 0:
        try:
            mo = statistics.mode(outcome)
            print("The avgerage was: " + str(mo))
            return outcome
        except statistics.StatisticsError:
            print("Both occured equally. Try again.")
            return 
    else: 
        outcome.append(random.randint(0,1))
    coinflips(times-1)
flips = 3
coinflips(flips)

loopout = []
for i in range(flips):
    loopout.append(random.randint(0,1))
try: 
    mo1 = statistics.mode(loopout)
    print('The average for the iteration was: ' + str(mo1))
except statistics.StatisticsError:
    print("Both occured equally. Try again.")
    