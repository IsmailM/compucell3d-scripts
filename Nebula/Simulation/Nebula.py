
import sys
from os import environ
from os import getcwd
import string

sys.path.append(environ["PYTHON_MODULE_PATH"])


import CompuCellSetup


sim,simthread = CompuCellSetup.getCoreSimulationObjects()
            
# add extra attributes here
            
CompuCellSetup.initializeSimulationObjects(sim,simthread)
# Definitions of additional Python-managed fields go here
        
#Add Python steppables here
steppableRegistry=CompuCellSetup.getSteppableRegistry()
        
from NebulaSteppables import NebulaSteppable, ForceSteppable

steppableRegistry.registerSteppable( NebulaSteppable(sim,_frequency=1) )
steppableRegistry.registerSteppable( ForceSteppable(sim,_frequency=1) )
        
CompuCellSetup.mainLoop(sim,simthread,steppableRegistry)
        
        