
from PySteppables import *
import CompuCell
import sys, os

from PySteppablesExamples import MitosisSteppableBase

## allows us to import the cc3dtools built.
pt = os.getcwd().split('/DivisionTracker/Simulation')[0]
sys.path.append(pt)

from cc3dtools.Genome import Genome, save_genomes

class ConstraintInitializerSteppable(SteppableBasePy):
    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
    def start(self):
        for cell in self.cellList:
            cell.targetVolume=25
            cell.lambdaVolume=2.0

class GrowthSteppable(SteppableBasePy):
    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
    def step(self,mcs):
        for cell in self.cellList:
            cell.targetVolume+=0.01 if cell.targetVolume != 0 else 0    
            if cell.targetVolume == 0 :
                print 'not growing',cell.targetVolume
            else:
                print 'growing',cell.targetVolume  

    # alternatively if you want to make growth a function of chemical concentration uncomment lines below and comment lines above        
        # field=CompuCell.getConcentrationField(self.simulator,"PUT_NAME_OF_CHEMICAL_FIELD_HERE")
        # pt=CompuCell.Point3D()
        # for cell in self.cellList:
            # pt.x=int(cell.xCOM)
            # pt.y=int(cell.yCOM)
            # pt.z=int(cell.zCOM)
            # concentrationAtCOM=field.get(pt)
            # cell.targetVolume+=0.01*concentrationAtCOM  # you can use here any fcn of concentrationAtCOM             
        

class MitosisSteppable(MitosisSteppableBase):
    def __init__(self,_simulator,_frequency=1, trackerInstance=None, genomes=[Genome(mutation_rate=0),Genome(mutation_rate=5)]):
        MitosisSteppableBase.__init__(self,_simulator, _frequency)
        self.trackerInstance = trackerInstance
        self.genomes = genomes
    
    def step(self,mcs):
        # print "INSIDE MITOSIS STEPPABLE"
        cells_to_divide=[]
        for cell in self.cellList:
            if cell.volume>28:
                print 'dividing now'
                cells_to_divide.append(cell)
        self.mcs=mcs        
        for cell in cells_to_divide:
            # to change mitosis mode leave one of the below lines uncommented
            self.divideCellRandomOrientation(cell)
            # self.divideCellOrientationVectorBased(cell,1,0,0)                 # this is a valid option
            # self.divideCellAlongMajorAxis(cell)                               # this is a valid option
            # self.divideCellAlongMinorAxis(cell)                               # this is a valid option

    def updateAttributes(self):
        parentCell=self.mitosisSteppable.parentCell
        childCell=self.mitosisSteppable.childCell
        print 'parent:',parentCell.id
        print 'child:',childCell.id
        genomes = self.genomes

        ## append a new genome to the genomes object
        genomes.append( genomes[parentCell.id].mutate().replicate() )
        # save the info of the division into our file
        
        self.trackerInstance.stashDivision( self.mcs , parentCell.id, childCell.id, parentCell.id )
        

        childCell.targetVolume=parentCell.targetVolume
        childCell.lambdaVolume=parentCell.lambdaVolume
        if parentCell.type==self.TUMOR:
            childCell.type=self.TUMOR
        else:
            childCell.type=self.TUMOR

    def finish(self):
        self.trackerInstance.saveStash()

        for k, genome in enumerate(self.genomes):
            print '-------      genome '+str(k)+'           ---------'
            print sorted(genome.get_mutated_loci())

        save_genomes(self.genomes, file_name='../gendata.csv')
        pass
        
        

class DeathSteppable(SteppableBasePy):
    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
    def step(self,mcs):
        if mcs==300:
            for cell in self.cellList:
                if cell.type==self.TUMOR:
                    cell.targetVolume=0
                    cell.lambdaVolume=100
                    print 'dying now\n\n\n\n\n\n\n\n'
