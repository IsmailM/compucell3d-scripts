
from PySteppables import *
import CompuCell
import sys

class NebulaSteppable(SteppableBasePy):    

    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
    def start(self):
        # any code in the start function runs before MCS=0
        pass
    def step(self,mcs):        
        #type here the code that will run every _frequency MCS
        for cell in self.cellList:
            print "cell.id=",cell.id
    def finish(self):
        # Finish Function gets called after the last MCS
        pass
        

class ForceSteppable(SteppableBasePy):    

    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
    def start(self):
        # any code in the start function runs before MCS=0
        pass
    def step(self,mcs):        
        #type here the code that will run every _frequency MCS

        location = CompuCell.Point3D()

        for cell in self.cellList:
            location.x = int(round(cell.xCOM))
            location.y = int(round(cell.yCOM))
            location.z = int(round(cell.zCOM))
            if location.y < 50:
                cell.lambdaVecY = +1
            else:
                cell.lambdaVecY = -1
            print location

    def finish(self):
        # Finish Function gets called after the last MCS
        pass
        