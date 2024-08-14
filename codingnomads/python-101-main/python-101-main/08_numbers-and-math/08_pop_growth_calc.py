# Variables
sp= 380123456 #starting population
pbs= 0.166666667 #people born per second
pds= 0.0833333333 #people dead per second
pis= 0.025 #people immigrating per second
spy= 31536000  #seconds per year
#formulas
pby= int(pbs*spy) #people born per year
piy= int(pis*spy) #people immigrating per year
pdy= int(pds*spy) #people dead per year
ppy= pby+piy-pds #population change per year
pop=sp+ppy
print(int(pop))