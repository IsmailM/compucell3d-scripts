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
        
from DiffusingFieldCellGrowthSteppables import DiffusingFieldCellGrowthSteppable, ConstraintInitializerSteppable, MitosisSteppable, MitosisDataPrinterSteppable

steppableRegistry.registerSteppable( ConstraintInitializerSteppable( sim ) )
steppableRegistry.registerSteppable( MitosisSteppable( sim ) )
steppableRegistry.registerSteppable( MitosisDataPrinterSteppable( sim ) )
steppableRegistry.registerSteppable( DiffusingFieldCellGrowthSteppable(sim,_frequency=1) )

CompuCellSetup.mainLoop(sim,simthread,steppableRegistry)
        
        