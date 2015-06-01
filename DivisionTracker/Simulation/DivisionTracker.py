
import sys
from os import environ
from os import getcwd
import string

sys.path.append(environ["PYTHON_MODULE_PATH"])

pt = os.getcwd().split('/DivisionTracker/Simulation')[0]+'/sim.csv'


import CompuCellSetup


sim,simthread = CompuCellSetup.getCoreSimulationObjects()
            
# add extra attributes here
            
CompuCellSetup.initializeSimulationObjects(sim,simthread)
# Definitions of additional Python-managed fields go here
        
#Add Python steppables here
steppableRegistry=CompuCellSetup.getSteppableRegistry()
        

from DivisionTrackerSteppables import ConstraintInitializerSteppable
ConstraintInitializerSteppableInstance=ConstraintInitializerSteppable(sim,_frequency=1)
steppableRegistry.registerSteppable(ConstraintInitializerSteppableInstance)
        

from DivisionTrackerSteppables import GrowthSteppable
GrowthSteppableInstance=GrowthSteppable(sim,_frequency=1)
steppableRegistry.registerSteppable(GrowthSteppableInstance)
        
from DivisionTrackerPackage import DivisionTracker

tracker = DivisionTracker(fileName='../division_output1615.csv')

from DivisionTrackerSteppables import MitosisSteppable

MitosisSteppableInstance=MitosisSteppable(sim,_frequency=1, trackerInstance=tracker)
steppableRegistry.registerSteppable(MitosisSteppableInstance)



from DivisionTrackerSteppables import DeathSteppable
DeathSteppableInstance=DeathSteppable(sim,_frequency=1)
steppableRegistry.registerSteppable(DeathSteppableInstance)
        
CompuCellSetup.mainLoop(sim,simthread,steppableRegistry)
        
