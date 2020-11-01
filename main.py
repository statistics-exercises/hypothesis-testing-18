import numpy as np

def standardDeviation( data ) :
  # Your code to calculate the standard deviation from the input data set goes here
  

# The code from here should not need to be adjusted.  It is there so you can 
# test the function you write
mydata = np.loadtxt("mydata.dat")
print( "The standardDeviation of the data set is", standardDeviation(mydata) )
