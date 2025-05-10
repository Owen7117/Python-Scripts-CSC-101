#Owen O'Neil
#2/13/24
#Program 3 Basic: Richter Scale

loop=0
while(loop==0):

    earthquake_power= float(input("The earthquake's magnitude on the Richter Scale: "))

    if (earthquake_power > 10.0):
        print("Richter scale does not extend beyond a practical maximum value of 10.0.") 
       
    if(earthquake_power < 0.0):
        print("Richter scale cannot be a negatve number.")
        

    def joules(scale): #cacluation for joules using Richtor scale
        j=10**((1.5*scale)+4.8)
        return j
    
    joules= joules(earthquake_power) #calling suberoutine to use in calculations
    tnt= joules/(4.184*10**9)
    volcano= joules/(8*10**17)
    nuke= joules/(6.3*10**13)
    
    if(earthquake_power <= 10 and earthquake_power>= 0):
        print("A {:,.4f} magnitude earthquake releases {:,.4f} joules of energy.".format(earthquake_power,joules))
        print("This is equivalent to {:,.4f} metric tons of exploded TNT.".format(tnt))
        print("This is equivalent to {:,.4f} Krakatoa eruptions and {:,.4f} Hiroshima bombs.".format(volcano, nuke))
        loop+=1 #ending loop if input is acceptable
        
         