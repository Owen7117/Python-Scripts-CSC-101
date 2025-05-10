#Owen O'Neil
#2/5/24
#Program2Basic: light travel

def sqrt(s):
    return(s**.5)
percent=float(input("Velocity as a % of the speed of light: "))
restingmass=float(input("Mass of the spaceship at rest (kg): "))
c= float(299792458)# speed of light
v= float(c*(percent/100))
movingmass=1/sqrt(1-(v**2/c**2))
mass = movingmass*restingmass 
print("Mass of spaceship: {:.3f} kg".format(mass))#new mass of spaceship
print("Time to travel to Alpha Centauri: {:.3f} light years".format(4.3/movingmass))
print("Time to travel to Bernard's Star: {:.3f} light years".format(6.0/movingmass))
print("Time to travel to Betelgeus: {:.3f} light years".format(309/movingmass))
print("Time to travel to Andromeda Galaxy: {:.3f} light years".format(2000000/movingmass))