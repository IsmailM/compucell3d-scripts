
from PySteppables import *
import CompuCell
import sys
class OscillatorySteppable(SteppableBasePy):    

    def __init__(self,_simulator,_frequency=10):
        SteppableBasePy.__init__(self,_simulator,_frequency)
    def start(self):
        # any code in the start function runs before MCS=0
        pass
    def step(self,mcs):        
        #type here the code that will run every _frequency MCS
        print 'SWITCHING OCCURING WOOT'
        for cell in self.cellList:
            if cell.type == self.CONDENSING:
                cell.type = self.NONCONDENSING
            elif cell.type == self.NONCONDENSING:
                cell.type = self.CONDENSING

    def finish(self):
        # Finish Function gets called after the last MCS
        pass
        