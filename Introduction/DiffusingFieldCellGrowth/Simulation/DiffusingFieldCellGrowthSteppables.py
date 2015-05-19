
from PySteppables import *
import CompuCell
import sys
from random import random
from PySteppablesExamples import MitosisSteppableBase



class DiffusingFieldCellGrowthSteppable(SteppableBasePy):    

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
        
class ConstraintInitializerSteppable(SteppableBasePy):

    def __init__(self, _simulator, _frequency=10):
        SteppableBasePy.__init__(self,_simulator,_frequency)
    
    def start(self):
        for cell in self.cellList:
            cell.targetVolume=25
            cell.lambdaVolume=2.0
            cellDictionary = CompuCell.getPyAttrib(cell)
            cellDictionary['relatives'] = []

    def step(self, mcs):
        field = CompuCell.getConcentrationField(self.simulator, "FGF")
        comPt = CompuCell.Point3D()

        for cell in self.cellList:
            if cell.type == self.CONDENSING:
                # get the coordinates of the current cells loation
                comPt.x = int(round(cell.xCOM))
                comPt.y = int(round(cell.yCOM))
                comPt.z = int(round(cell.zCOM))

                # use the point to get the concentration at this location
                conc = field.get(comPt)
                cell.targetVolume += 0.1 * conc
                
    def finish(self):
        pass

class MitosisData(object):
    def __init__(self, MCS=0, parentId=01, parentType=-1, offspringId=-1, offspringType=-1):
        self.MCS = MCS
        self.parentType = parentType
        self.parentId = parentId
        self.offspringType = offspringType
        self.offspringId = offspringId

    def __str__(self):
        return "Time of mitosis %s, parentId %s, parentType %s"%(str(self.MCS), str(self.parentId), str(self.parentType))

class MitosisSteppable(MitosisSteppableBase):

    def __init__(self, _simulator, _frequency=1):
        MitosisSteppableBase.__init__(self,_simulator,_frequency)
    

    def step(self, mcs):

        for cell in self.cellList:
            if cell.volume > 50:
                self.divideCellRandomOrientation(cell)


    def updateAttributes(self):

        # self.mitosisSteppable holds important dat from the mitosis
        parentCell = self.mitosisSteppable.parentCell
        childCell = self.mitosisSteppable.childCell

        parentCell.targetVolume/=2.0

        #child inherits parent properties
        childCell.targetVolume = parentCell.targetVolume
        childCell.lambdaVolume = parentCell.lambdaVolume

        # randomly select one of the cells to be a different type
        if random()<0.5:
            childCell.type = parentCell.type
        else:
            childCell.type = self.DIFFERENTIATEDCONDENSING


        # get parent cell lists
        parentDict = CompuCell.getPyAttrib(parentCell)
        childDict = CompuCell.getPyAttrib(childCell)


        mcs=self.simulator.getStep()

        data = MitosisData(mcs, parentCell.id, parentCell.type, childCell.id, childCell.type)
        childDict['relatives'] = [data]
        parentDict['relatives'].append(data)


class MitosisDataPrinterSteppable(SteppableBasePy):

    def __init__(self, _simulator, _frequency=100):
        SteppableBasePy.__init__(self,_simulator,_frequency)
    

    def step(self, mcs):
        for cell in self.cellList:
            dataList = CompuCell.getPyAttrib(cell)
            if len(dataList['relatives'])>0:
                print "MITOTIC DATA FOR CELL ID:",cell.id
                for data in dataList['relatives']:
                    print data
    def finish(self):
        for cell in self.cellList:
            dataList = CompuCell.getPyAttrib(cell)
            if len(dataList['relatives'])>0:
                print "MITOTIC DATA FOR CELL ID:",cell.id
                for data in dataList['relatives']:
                    print data

