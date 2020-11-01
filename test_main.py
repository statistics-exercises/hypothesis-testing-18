import unittest
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_standard_deviation(self) : 
        myd = np.loadtxt("mydata.dat")
        av = sum(myd) / len(myd)
        av2 = sum(myd*myd) / len(myd)
        myvar = ( len(myd) / (len(myd) - 1) )*( av2 - av*av )
        self.assertTrue( np.abs( np.sqrt(myvar) - standardDeviation(myd) )<1e-7, "Your function for computing the standard deviation is not giving the correct result" )
